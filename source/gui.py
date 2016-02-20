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
        self.reloading_progress.font = self.font

        # Charger clip init
        self.charger_clip = ChargerClip()
        self.charger_clip.font = self.font

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

        # Registering listeners for events
        self.event_dispatcher.add_event_listener(GameEvent.RELOAD_START, self.reloading_progress.on_reload_start)
        self.event_dispatcher.add_event_listener(GameEvent.DAMAGE_GOT, self.health_bar.on_damage_got)
        self.event_dispatcher.add_event_listener(GameEvent.AMMO_SHOT, self.charger_clip.on_ammo_shot)
        self.event_dispatcher.add_event_listener(GameEvent.SCORE_GOT, self.score.on_score_got)

    def update(self):
        # Update all
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

    def on_score_got(self, event):
        assert isinstance(event.data, int)
        self.score += event.data

    def update(self):
        """
        Renders new score on screen
        """
        score_text = self.font.render(str(self.score), 1, (255, 255, 255))
        pygame.display.get_surface().blit(score_text, (1000, 20))


class HealthBar(object):
    def __init__(self):
        self.size = (200, 50)
        self.image = pygame.Surface(self.size)
        self.image.fill(pygame.Color("#00ff00"))

        self.max_health = 0

    def on_damage_got(self, event):
        assert isinstance(event, GameEvent)
        assert isinstance(event.data, Player)

        if not self.max_health:
            self.max_health = event.data.MAX_HEALTH

        curr_width = int(self.size[0] * event.data.curr_health / self.max_health)
        self.image.fill(pygame.Color("#ff0000"))
        pygame.draw.rect(self.image, pygame.Color("#00ff00"), pygame.Rect(0, 0, curr_width, self.size[1]))

    def update(self):
        pygame.display.get_surface().blit(self.image, (5, 5))


class ReloadingProgress(object):
    """
    Reloading progress bar
    """

    def __init__(self):
        self.font = None
        self.reloading = False
        self.counter = 0

    def update(self):
        if self.reloading:
            if self.counter:
                # TODO Set appropriate coordinates
                reload_text = self.font.render("Reloading", 1, (255, 255, 255))
                pygame.display.get_surface().blit(reload_text, (100, 400))
                self.counter -= 1
            else:
                self.reloading = False

    def on_reload_start(self, event):
        """
        Event handler method
        :param event: event from weapon
        """
        assert isinstance(event, GameEvent)
        assert isinstance(event.data, Weapon)
        self.reloading = True
        self.counter = event.data.RELOAD_TIME


class ChargerClip(object):
    """
    Visualisation of remaining ammo in clip
    """

    def __init__(self):
        self.font = None
        self.curr_ammo = 0

    def update(self):
        # TODO Set appropriate coordinates
        score_text = self.font.render(str(self.curr_ammo), 1, (255, 255, 255))
        pygame.display.get_surface().blit(score_text, (100, 500))

    def on_ammo_shot(self, event):
        #TODO Implement
        assert isinstance(event, GameEvent)
        assert isinstance(event.data, Weapon)
        self.curr_ammo = event.data.shots