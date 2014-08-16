# -*- coding: utf-8 -*-
__author__ = 'matanaliz'

from gui import Gui
from entities import *


class Game(object):
    def __init__(self, width=1280, height=720, fps=120):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.wave = 0

        self.font = pygame.font.Font(None, 30)
        self.score = 0

        self.event_dispatch = EventDispatcher()

        #Init all user interface staff
        self.gui = Gui()
        self.gui.set_event_dispatcher(self.event_dispatch)

        #Init all entities
        self.entities = Entities()
        self.entities.set_event_dispatcher(self.event_dispatch)

    def run(self):
        while True:
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                break

            self.clock.tick(self.fps)
            self.screen.fill(pygame.Color("#3d863d"))

            self.entities.update()
            self.gui.update()

            pygame.display.flip()

        pygame.quit()

    def display_gameover(self):
        font = pygame.font.Font(None, 72)
        text = font.render("WASTED", 1, (255, 255, 255))
        #TODO: Bad idea. Later: why? Comment more clearly
        self.screen.blit(text, (640, 360))


if __name__ == '__main__':
    Game().run()