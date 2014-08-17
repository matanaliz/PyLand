# -*- coding: utf-8 -*-
__author__ = 'matanaliz'

import pygame
from player import Player
from enemy import Enemy
from weapon import Shotgun
from event import *
import random


class Entities(object):
    """
    Hold up player, bullets, enemies, gui entities for proper render and collision detection
    """

    def __init__(self):
        #Sprite groups init
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.foe_group = pygame.sprite.Group()

        #Init enemy generating values. Should be changed.
        self.count = 10
        self.wave = 0

        self.player = Player(pygame.display.get_surface().get_rect())
        #TODO pass player position, not whole
        weapon = Shotgun(self.player, self.bullet_group)
        self.player.give_weapon(weapon)
        self.player_group.add(self.player)

        self.event_dispatcher = 0

    def set_event_dispatcher(self, event_dispatcher):
        """
        Setting event dispatcher
        :param event_dispatcher:
        """
        assert isinstance(event_dispatcher, EventDispatcher)
        self.event_dispatcher = event_dispatcher

        #Apply event dispatcher for all other
        self.player.set_event_dispatcher(event_dispatcher)

    def generate_foes(self):
        #Add more stronger enemies with waves
        self.wave += 1

        screen_rect = pygame.display.get_surface().get_rect()

        #Adding more same enemies with waves
        for i in range(self.count + (self.wave * 2)):
            pos = (self.random_two_period(-200, 0, screen_rect.height, screen_rect.height + 200),
                   self.random_two_period(-200, 0, screen_rect.height, screen_rect.height + 200))
            enemy = Enemy(self.player, pos)
            enemy.foe_group = self.foe_group
            if not pygame.sprite.spritecollideany(enemy, self.foe_group):
                self.foe_group.add(enemy)

    @staticmethod
    def random_two_period(start1, end1, start2, end2):
        return random.choice([random.randint(start1, end1), random.randint(start2, end2)])

    def check_for_collision(self):
        #Check player collision
        foe = pygame.sprite.spritecollideany(self.player, self.foe_group)
        if foe is not None:
            #Do something if player is dead
            self.player.apply_damage(foe.attack())
        else:
            collision_dict = pygame.sprite.groupcollide(self.bullet_group, self.foe_group, False, False)
            for bullet, foes in collision_dict.iteritems():
                for foe in foes:
                    if foe.apply_damage(bullet.get_damage()):
                        #Dispatch event to health bar
                        if self.event_dispatcher:
                            self.event_dispatcher.dispatch_event(GameEvent(GameEvent.SCORE_GOT, foe.get_score()))
                        foe.kill()

                    #Bullet is removed if was collided
                    bullet.kill()

    def update(self):

        #Check for collisions
        self.check_for_collision()
        if len(self.foe_group) <= 1:
            #Generate more enemies.
            self.generate_foes()

        screen = pygame.display.get_surface()

        self.player_group.update()
        self.player_group.draw(screen)

        self.bullet_group.update()
        self.bullet_group.draw(screen)

        self.foe_group.update()
        self.foe_group.draw(screen)

        #Generate foes
