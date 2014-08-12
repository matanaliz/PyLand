__author__ = 'matanaliz'

import pygame
from common import *
from player import Player


class Enemy(pygame.sprite.Sprite):
    #TODO Speed changes with damage or other mechanics
    __speed__ = 2
    #TODO Add health bar for enemies
    __health__ = 100
    __color__ = pygame.Color("#fff000")
    #Some aliens can shoot!
    #TODO Give weapons to aliens
    __weapon__ = None
    #Decreasing player health bar
    __melee_damage__ = 10
    __score__ = 50

    def __init__(self, group, player_obj, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self, group)

        assert isinstance(player_obj, Player)

        self.size = (32, 32)
        self.image = pygame.Surface(self.size)
        self.rect = pygame.Rect(pos[0], pos[1], *self.size)
        self.image.fill(self.__color__)

        self.player = player_obj

    def get_pos(self):
        return self.rect.center

    def get_score(self):
        return self.__score__

    def update(self):
        direction = normalize(sub(self.player.rect.center, self.get_pos()))
        self.rect.move_ip(*[x * self.__speed__ for x in direction])

    def apply_damage(self, damage):
        if self.__health__ > damage:
            self.__health__ -= damage
            return False
        else:
            return True


class YellowAlien(Enemy):
    __speed__ = 1
    __health__ = 500
    __color__ = pygame.Color("#fff000")
    __weapon__ = None
    __score__ = 60

    def __init__(self, group, player_obj, pos=(0, 0)):
        Enemy.__init__(group, player_obj, pos)
