__author__ = 'matanaliz'

import pygame
import random
from player import Player
from enemy import *

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

    def run(self):

        entities = pygame.sprite.Group()
        foes = pygame.sprite.Group()
        player = Player(entities, self.screen.get_rect())

        #Generatin enemies
        self.generate_foes(foes, player, 10, self.width, self.height)

        entities.add(player)

        while True:
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                break

            self.clock.tick(self.fps)
            self.screen.fill(pygame.Color("#000000"))

            self.display_score(self.score, self.screen)

            entities.update()
            entities.draw(self.screen)

            foes.update()
            foes.draw(self.screen)

            self.check_for_collision(player, entities, foes)
            if len(foes) <= 1:
                #Generate more enemies.
                self.generate_foes(foes, player, 10, self.width, self.height)

            pygame.display.flip()

        pygame.quit()

    def check_for_collision(self, player, entities, foes):
        #Check player collision
        if not pygame.sprite.spritecollideany(player, foes) == None:
            #GAME OVER or other mechanics
            self.display_gameover(self.screen)
            #Should stop the game
            print "GAME OVER"

        else:
            coll_dict = pygame.sprite.groupcollide(entities, foes, False, False)
            for bullet, foes in coll_dict.iteritems():
                for foe in foes:
                    if foe.apply_damage(bullet.get_damage()):
                        #Add some score or other mechanics
                        self.score += foe.get_score()
                        foe.kill()
                    else:
                        bullet.kill()

    def generate_foes(self, foes, player, count, width, height):

        #Add more stronger enemies with waves
        self.wave += 1

        #Generating enemies out of screen
        h_range = range(-200, 0) + range(height, height + 200)
        w_range = range(-200, 0) + range(width, width + 200)

        #Adding more same enemies with waves
        for i in range(count + (self.wave * 2)):
            foes.add(Enemy(foes, player, (random.choice(h_range), random.choice(w_range))))

    def display_score(self, score, screen):
        score_text = self.font.render("Score: " + str(score), 1, (255, 255, 255))
        #Bad idea
        screen.blit(score_text, (1000, 20))

    def display_gameover(self, screen):
        font = pygame.font.Font(None, 72)
        text = font.render("WASTED", 1, (255, 255, 255))
        #Bad idea
        screen.blit(text, (640, 360))


if __name__ == '__main__':
    Game().run()