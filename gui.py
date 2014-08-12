# -*- coding: utf-8 -*-
__author__ = 'matanaliz'


class Gui(object):
    """
    Adapter object that holds all UI things
    """

    def __init__(self):
        pass

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


class Score(object):
    def __init__(self, common_font):
        pass


class HealthBar(object):
    def __init__(self, health_listener):
        pass


class ReloadingProgress(object):
    """
Reloading progress bar
"""

    def __init__(self, weapon_listener):
        """
    Presetting weapon listener
    :param weapon_listener: Recharge listener from weapon object
    """
        pass

    def update(self):
        """
    Updates reloading sprite (sidedar with percetage)
    """


class ChargerClip(object):
    """
Visualisation of remaining ammo in clip
"""

    def __init__(self, weapon_listener):
        pass

    def update(self):
        pass