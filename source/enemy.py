# -*- coding: utf-8 -*-
__author__ = 'matanaliz'

import pygame
from common import *
from player import Player


class Enemy(pygame.sprite.Sprite):
    """
    Base enemy class
    """
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

    def __init__(self, player_obj, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        assert isinstance(player_obj, Player)

        self.size = (32, 32)

        #Transparent surface
        self.image = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.rect = pygame.Rect(pos[0], pos[1], *self.size)

        pygame.draw.rect(self.image, pygame.Color("#fff000"), pygame.Rect(0, 0, 32, 32))
        #Saving base image for rotation
        self.base_image = self.image

        self.player = player_obj

        self.curr_pos = self.rect.center

    def get_pos(self):
        return self.rect.center

    def get_score(self):
        return self.BOUNTY

    def update(self):
        direction = normalize(sub(self.player.rect.center, self.get_pos()))
        move_vec = mul(direction, self.SPEED)

        self.curr_pos = add(self.curr_pos, move_vec)

        #Rotating to face player
        self.__rotate(angle(direction))
        self.rect.center = self.curr_pos

    def apply_damage(self, damage):
        if self.HEALTH > damage:
            self.HEALTH -= damage
            return False
        else:
            return True

    def attack(self):
        #TODO: Melee damage colldown
        return self.MELEE_DAMAGE

    def __rotate(self, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = self.rect
        self.image = pygame.transform.rotate(self.base_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = orig_rect.center


class YellowAlien(Enemy):
    SPEED = 1
    HEALTH = 500

    def __init__(self, group, player_obj, pos=(0, 0)):
        Enemy.__init__(group, player_obj, pos)
