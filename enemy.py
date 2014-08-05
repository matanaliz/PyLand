__author__ = 'oleksandr.kaspruk'

import pygame
from common import *
from player import Player

class Enemy(pygame.sprite.Sprite):

    __speed__  = 2
    __health__ = 1000

    def __init__(self, group, playerObj, pos = (0, 0)):
        pygame.sprite.Sprite.__init__(self, group)

        assert isinstance(playerObj, Player)

        self.size = (32, 32)
        self.image = pygame.Surface(self.size)
        self.rect = pygame.Rect(pos[0], pos[1], *self.size)
        self.image.fill(pygame.Color("#fff000"))

        self.player = playerObj

    def get_pos(self):
        return self.rect.center

    def update(self):
        direction = normalize(sub(self.player.rect.center, self.get_pos()))
        self.rect.move_ip(*[x * self.__speed__ for x in direction])

    def apply_damage(self, damage):
        if self.__health__ > damage:
            self.__health__ -= damage
            return False
        else:
            self.kill()
            return True