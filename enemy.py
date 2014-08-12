# -*- coding: utf-8 -*-
__author__ = 'matanaliz'

import pygame
from common import *
from player import Player


class Enemy(pygame.sprite.Sprite):
    #TODO Speed changes with damage or other mechanics
    SPEED = 2
    #TODO Add health bar for enemies
    HEALTH = 150

    #Some aliens can shoot!
    #TODO Give weapons to aliens
    WEAPON = None
    #Decreasing player health bar
    MELEE_DAMAGE = 10
    BOUNTY = 42

    def __init__(self, group, player_obj, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self, group)

        assert isinstance(player_obj, Player)

        self.size = (32, 32)
        self.image = pygame.Surface(self.size)
        self.rect = pygame.Rect(pos[0], pos[1], *self.size)
        self.image.fill(pygame.Color("#fff000"))

        self.player = player_obj

    def get_pos(self):
        return self.rect.center

    def get_score(self):
        return self.BOUNTY

    def update(self):
        direction = normalize(sub(self.player.rect.center, self.get_pos()))
        self.rect.move_ip(*[x * self.SPEED for x in direction])

    def apply_damage(self, damage):
        if self.HEALTH > damage:
            self.HEALTH -= damage
            return False
        else:
            return True


class YellowAlien(Enemy):
    SPEED = 1
    HEALTH = 500

    def __init__(self, group, player_obj, pos=(0, 0)):
        Enemy.__init__(group, player_obj, pos)
