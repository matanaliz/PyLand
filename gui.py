# -*- coding: utf-8 -*-
__author__ = 'matanaliz'

import pygame
from weapon import Weapon
from player import Player
from event import *


class Gui(object):
    """
    Adapter object that holds all UI things
    """

    def __init__(self):
        self.font = pygame.font.Font(None, 30)

        self.score = Score(self.font)
        self.health_bar = HealthBar()
        self.reloading_progress = ReloadingProgress()
        self.charger_clip = ChargerClip()

        self.update_list = [
            self.score,
            self.health_bar,
            self.reloading_progress,
            self.charger_clip
        ]

        self.event_dispatcher = 0

    def set_event_dispatcher(self, event_dispatcher):
        """
        Setting event dispatcher
        :param event_dispatcher:
        """
        assert isinstance(event_dispatcher, EventDispatcher)
        self.event_dispatcher = event_dispatcher

        #Registering listeners for events
        self.event_dispatcher.add_event_listener(GameEvent.RELOAD_START, self.reloading_progress.on_reload_start)
        self.event_dispatcher.add_event_listener(GameEvent.DAMAGE_GOT, self.health_bar.on_damage_got)
        self.event_dispatcher.add_event_listener(GameEvent.AMMO_SHOT, self.charger_clip.on_ammo_shot)

    def update_score(self, score):
        """
        Renders new score on screen
        :param score:
        """
        #Lol. Such a shame. Should clear this up.
        self.score.score = score

    def update(self):
        #Update all
        for obj in self.update_list:
            obj.update()


class Score(object):
    """
    Class that represents score object
    """
    def __init__(self, common_font):
        assert isinstance(common_font, pygame.font.Font)
        self.font = common_font
        self.score = 0

    def update(self):
        """
        Renders new score on screen
        :param score:
        """
        score_text = self.font.render(str(self.score), 1, (255, 255, 255))
        pygame.display.get_surface().blit(score_text, (1000, 20))

class HealthBar(object):
    def __init__(self):
        self.size = (200, 50)
        self.image = pygame.Surface(self.size)
        self.image.fill(pygame.Color("#ffffff"))

        self.max_health = 0

    def on_damage_got(self, event):
        assert isinstance(event, GameEvent)
        assert isinstance(event.data, Player)

        if not self.max_health:
            self.max_health = event.data.MAX_HEALTH

        curr_width = int(self.size[0] * event.data.curr_health / self.max_health)
        print curr_width
        self.image = pygame.Surface((curr_width, self.size[1]))
        #TODO change color with health percentage
        self.image.fill(pygame.Color("#ffffff"))

    def update(self):
        pygame.display.get_surface().blit(self.image, (5, 5))


class ReloadingProgress(object):
    """
    Reloading progress bar
    """

    def __init__(self):
        """
        """
        pass

    def update(self):
        """
        Updates reloading sprite (sidebar with percentage)
        """
        pass

    def on_reload_start(self, event):
        """
        Event handler method
        :param event: event from weapon
        """
        assert isinstance(event, GameEvent)
        assert isinstance(event.data, Weapon)


class ChargerClip(object):
    """
    Visualisation of remaining ammo in clip
    """

    def __init__(self):
        pass

    def update(self):
        pass

    def on_ammo_shot(self, event):
        assert isinstance(event, GameEvent)
        assert isinstance(event.data, Weapon)

