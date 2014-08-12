__author__ = 'matanaliz'

import pygame
import random
from common import *


class Bullet(pygame.sprite.Sprite):

    #TODO: Should be for custom image
    SPEED = 10.0
    MAX_RANGE = 1000
    DAMAGE = 15
    SIZE = (3, 3)

    def __init__(self, group, direction, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self, group)

        self.image = pygame.Surface(self.SIZE)
        self.image.fill(pygame.Color("#ffcc00"))

        self.rect = pygame.Rect(pos, self.SIZE)
        self.origin_center = self.rect.center
        self.direction = direction
        self.new_pos = []
        self.path = 0

        self.age = 1
        self.speed = self.SPEED + random.uniform(-1.0, 1.0)

    def update(self):
        self.age += 1
        self.new_pos = [x * self.speed * self.age for x in self.direction]
        self.path = magnitude(self.new_pos)

        self.rect.center = add(self.origin_center, self.new_pos)

        #Cheching path or age
        if self.path > self.MAX_RANGE:
            self.kill()

    def set_size(self, size):
        assert isinstance(size, object)
        self.SIZE = size

    def set_speed(self, speed):
        self.SPEED = speed
        self.speed = self.SPEED + random.uniform(-2.0, 2.0)

    def set_range(self, max_path):
        self.MAX_RANGE = max_path

    def get_damage(self):
        return self.DAMAGE


class Weapon(object):
    #Speed and range can be different for different guns
    #Default values
    #TODO: Hide into bullet
    BULLET_SPEED = 10
    BULLET_RANGE = 1000

    #In ticks
    __reload_time__ = 100
    __bullet_reload_time__ = 50

    #TODO: Add semi-auto weapon mode
    __semi_auto__ = False

    #Capacity
    __capacity__ = 10

    def __init__(self, owner, group, bullet_cls):
        #Fire rate and reload variables
        self.bullet_reload_timer = 0
        self.reloading_timer = 0
        self.reloading = False
        self.bullet_reloading = False
        self.shots = 0

        self.bullet_group = group
        self.owner = owner
        #TODO Assertion error. investigate inheritance error
        #assert isinstance(bullet_cls, Bullet)
        self.bullet_cls = bullet_cls

    def fire(self, where):
        if self.can_shoot():
            direction = normalize(sub(where, self.get_pos()))
            #Creating bullet of custom class
            bullet = self.bullet_cls(self.bullet_group, direction, self.get_pos())
            bullet.set_speed(self.BULLET_SPEED)
            bullet.set_range(self.BULLET_RANGE)
            self.bullet_group.add(bullet)

    def can_shoot(self):
        if self.shots <= self.__capacity__:
            if not self.bullet_reloading:
                self.shots += 1
                self.bullet_reloading = True
                return True
            else:
                return False
        else:
            self.reloading = True
            return False

    def tick(self):
        if self.bullet_reloading:
            if self.bullet_reload_timer < self.__bullet_reload_time__:
                self.bullet_reload_timer += 1
            else:
                self.bullet_reload_timer = 0
                self.bullet_reloading = False

        if self.reloading:
            if self.reloading_timer < self.__reload_time__:
                self.reloading_timer += 1
            else:
                self.shots = 0
                self.reloading_timer = 0
                self.reloading = False

    def get_pos(self):
        return self.owner.rect.center


class PistolBullet(Bullet):
    DAMAGE = 60
    SIZE = (3, 3)

    def __init__(self, group, direction, pos=(0, 0)):
        Bullet.__init__(self, group, direction, pos)


#TODO: Read weapons from xml
class Pistol(Weapon):
    __bullet_speed__ = 10
    __bullet_range__ = 1000

    def __init__(self, owner, group):
        Weapon.__init__(self, owner, group, PistolBullet)


class ShotgunBullet(Bullet):
    DAMAGE = 20
    SIZE = (3, 3)

    def __init__(self, group, direction, pos=(0, 0)):
        Bullet.__init__(self, group, direction, pos)


class Shotgun(Weapon):
    BULLET_SPEED = 18
    BULLET_RANGE = 900

    def __init__(self, owner, group):
        Weapon.__init__(self, owner, group, ShotgunBullet)

        #May be misunderstanding. This is how many shots will be produced in one shot by shotgun
        self.__shots_count = 15

    def fire(self, where):
        where_list = []
        for _ in range(self.__shots_count):
            where_list.append((where[0] + random.randint(-20, 20), where[1] + random.randint(-20, 20)))

        direct_list = [normalize(sub(where, self.get_pos())) for where in where_list]

        if self.can_shoot():
            for direction in direct_list:
                #Creating bullet of custom class
                bullet = self.bullet_cls(self.bullet_group, direction, self.get_pos())
                #??? Remove this from here
                bullet.set_speed(self.BULLET_SPEED)
                bullet.set_range(self.BULLET_RANGE)
                self.bullet_group.add(bullet)