__author__ = 'matanaliz'

import pygame
import random
from player import Player
from enemy import Enemy

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
        foes = pygame.sprite.Group()
        player = Player(entities, self.screen.get_rect())
        #Should add some levels. List of enemies
        #enemy = Enemy(foes, player, (0, 0))
        self.generate_foes(foes, player, 10, self.width, self.height)

        entities.add(player)
        #foes.add(enemy)

        while True:
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                break

            self.clock.tick(self.fps)
            self.screen.fill(pygame.Color("#000000"))

            entities.update()
            entities.draw(self.screen)

            foes.update()
            foes.draw(self.screen)

            self.check_for_collision(player, entities, foes)

            pygame.display.flip()

        pygame.quit()

    def check_for_collision(self, player, entities, foes):
        #Check player collision
        if not pygame.sprite.spritecollideany(player, foes) == None:
            #GAME OVER or other mechanics
            print "GAME OVER"

        else:
            coll_dict = pygame.sprite.groupcollide(entities, foes, False, False)
            for bullet, foe in coll_dict.iteritems():
                if foe[0].apply_damage(bullet.get_damage()):
                    #Add some score or other mechanics
                    print "Foe was killed"
                else:
                    bullet.kill()

    def generate_foes(self, foes, player, count, width, height):

        h_range = range(-200, 0) + range(height, height + 200)
        w_range = range(-200, 0) + range(width, width + 200)

        for i in range(count):
            foes.add(Enemy(foes, player, (random.choice(h_range), random.choice(w_range))))





####
if __name__ == '__main__':
    Game().run()