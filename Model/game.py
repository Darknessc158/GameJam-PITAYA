import sys

import pygame
from pygame.locals import *


class Game:
    
    def __init__(self, score, time):
        self.score = score
        self.time = time

    def get_score(self):
        return self.score

    def get_time(self):
        return self.time

    def add_score(self, altitude):
        self.score += altitude

    def set_time(self, time):
        self.time = time

    def game(self, mainClock):
        running = True
        while running:            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)
