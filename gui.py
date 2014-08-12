# -*- coding: utf-8 -*-
__author__ = 'matanaliz'

import pygame
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

        self.event_dispatcher = 0

    def set_event_dispatcher(self, event_dispatcher):
        assert isinstance(event_dispatcher, EventDispatcher)
        self.event_dispatcher = event_dispatcher

        #Registering listeners for events
        self.event_dispatcher.add_event_listener(GameEvent.RELOAD_START, self.reloading_progress.on_reload_start)
        self.event_dispatcher.add_event_listener(GameEvent.DAMAGE_GOT, self.health_bar.on_damage_got)
        self.event_dispatcher.add_event_listener(GameEvent.AMMO_SHOT, self.charger_clip.on_ammo_shot)

    def change_font(self, new_font):
        """
        Changes font on new one
        :param new_font:
        """

    def set_weapon_listener(self, weapon_listener):
        """

        :param weapon_listener:
        """
        pass

    def set_health_listener(self, health_listener):
        pass

    def update_score(self, score):
        self.score.display_score(score)


class Score(object):
    def __init__(self, common_font):
        assert isinstance(common_font, pygame.font.Font)
        self.font = common_font

    def display_score(self, score):
        score_text = self.font.render(str(score), 1, (255, 255, 255))
        pygame.display.get_surface().blit(score_text, (1000, 20))


class HealthBar(object):
    def __init__(self):
        pass

    def on_damage_got(self, event):
        pass


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
        Updates reloading sprite (sidedar with percetage)
        """
        pass

    def on_reload_start(self, event):
        print 'reload start'


class ChargerClip(object):
    """
Visualisation of remaining ammo in clip
"""

    def __init__(self):
        pass

    def update(self):
        pass

    def on_ammo_shot(self, event):
        print 'shot!'