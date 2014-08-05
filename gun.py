__author__ = 'matanaliz'

import pygame
from common import *

class Gun(object):

    #Speed and range can be different for different guns
    #Default values
    __bullet_speed__ = 10
    __bullet_range__ = 1000
    #Should consider something with fire rate
    __fire_rate__    = 10

    def __init__(self, owner, group, BulletObj):

        self.bullets = group
        self.owner = owner
        self.bullet = BulletObj

    def fire(self, where):
        direction = normalize(sub(where, self.get_pos()))
        #Creating bullet of custom class
        bullet = self.bullet(self.bullets, direction, self.get_pos())
        bullet.set_speed(self.__bullet_speed__)
        bullet.set_range(self.__bullet_range__)
        self.bullets.add(bullet)

    def get_pos(self):
        return self.owner.rect.center

class Bullet(pygame.sprite.Sprite):

    #Should be for custom image
    __speed__    = 10
    __max_path__ = 1000
    __damage__   = 15
    __size__     = (3, 3)

    def __init__(self, group, direction, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self, group)

        self.image = pygame.Surface(self.__size__)
        self.image.fill(pygame.Color("#ff0000"))

        self.rect = pygame.Rect(pos, self.__size__)
        self.origin_center = self.rect.center
        self.direction = direction
        self.age = 1

    def update(self):
        self.age += 1
        self.path = [x * self.__speed__ * self.age for x in self.direction]

        self.rect.center = add(self.origin_center, self.path)

        #Add collision code
        if magnitude(self.path) > self.__max_path__:
            self.kill()

    def set_size(self, size):
        self.size = size

    def set_speed(self, speed):
        self.__speed__ = speed

    def set_range(self, range):
        self.__max_path__ = range

    def get_damage(self):
        return self.__damage__


class Pistol(Gun):
    __bullet_speed__ = 10
    __bullet_range__ = 1000

    def __init__(self, owner, group):
        Gun.__init__(self, owner, group, PistolBullet)

class PistolBullet(Bullet):
    __damage__  = 11
    __size__    = (3, 3)
    def __init__(self, group, direction, pos=(0, 0)):
        Bullet.__init__(self, group, direction, pos)