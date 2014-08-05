__author__ = 'matanaliz'

import pygame
from player import Player

class Game(object):
    def __init__(self, width=1280, height=720, fps=120):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.clock = pygame.time.Clock()
        self.fps = fps

    def run(self):
        entities = pygame.sprite.Group()
        player = Player(entities)
        player.bound = self.screen.get_rect()

        entities.add(player)

        while True:
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                break

            self.clock.tick(self.fps)
            self.screen.fill(pygame.Color("#000000"))

            entities.update()
            entities.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

####
if __name__ == '__main__':
    Game().run()