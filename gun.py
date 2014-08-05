__author__ = 'matanaliz'

import pygame
import random
from common import *

class Gun(object):

    #Speed and range can be different for different guns
    #Default values
    __bullet_speed__ = 10
    __bullet_range__ = 1000

    #In ticks
    __reload_time__  = 60
    __fire_rate__    = 30

    #Capacity
    __capacity__     = 10

    def __init__(self, owner, group, BulletObj):

        self.bullets = group
        self.owner = owner
        self.bullet = BulletObj
        self.shots = 0

        #Fire rate and reload variables
        self.last_shot = 0
        self.last_reload = 0

    def fire(self, where):
        if self.can_i_shoot():
            direction = normalize(sub(where, self.get_pos()))
            #Creating bullet of custom class
            bullet = self.bullet(self.bullets, direction, self.get_pos())
            bullet.set_speed(self.__bullet_speed__)
            bullet.set_range(self.__bullet_range__)
            self.bullets.add(bullet)

    def can_i_shoot(self):
        if self.shots <= self.__capacity__ or self.shots == 0:
            if self.last_shot == 0:
                self.last_shot = 1
                self.shots += 1
                return True
        else:
            self.last_reload = 1
            return False


    def tick(self):
        if self.last_shot > 0 and self.last_shot < self.__fire_rate__:
            self.last_shot += 1
        else:
            self.last_shot = 0

        if self.last_reload > 0 and self.last_reload < self.__reload_time__:
            self.last_reload += 1
        elif self.last_reload == self.__reload_time__:
            self.last_reload = 0
            self.shots = 0

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

#Read weapons from xml
class Pistol(Gun):
    __bullet_speed__ = 10
    __bullet_range__ = 1000

    def __init__(self, owner, group):
        Gun.__init__(self, owner, group, PistolBullet)

class PistolBullet(Bullet):
    __damage__  = 60
    __size__    = (3, 3)
    def __init__(self, group, direction, pos=(0, 0)):
        Bullet.__init__(self, group, direction, pos)

class ShotgunBullet(Bullet):
    __damage__  = 90
    __size__    = (3, 3)
    def __init__(self, group, direction, pos=(0, 0)):
        Bullet.__init__(self, group, direction, pos)

class Shotgun(Gun):
    __bullet_speed__ = 15
    __bullet_range__ = 800
    def __init__(self, owner, group):
        Gun.__init__(self, owner, group, ShotgunBullet)

    def fire(self, where):
        where_list = [(where[0] + random.randint(-50, 50), where[1] + random.randint(-50, 50)) for _ in range(7)]
        direct_list = [normalize(sub(where, self.get_pos())) for where in where_list]

        if self.can_i_shoot():
            for direction in direct_list:
                print direction
                #Creating bullet of custom class
                bullet = self.bullet(self.bullets, direction, self.get_pos())
                #??? Remove this from here
                bullet.set_speed(self.__bullet_speed__)
                bullet.set_range(self.__bullet_range__)
                self.bullets.add(bullet)