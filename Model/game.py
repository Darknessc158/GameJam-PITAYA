import sys
sys.path.append('../GameJam-PITAYA/View')
import pygame
from pygame.locals import *
from Model.objet import Objet
from Model.objet import Carburant
import random


class Game:
    
    def __init__(self, score, time):
        self.score = score
        self.time = time

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score

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

    def generate_objet(self):
        i = 0
        x = 0
        y = 0
        powerups = []
        while i < 5: # 1ere 5 carburants
            i += 1
            x = int(random.random()*1000)
            y = int(-random.random()*1000)
            carb = Carburant("carburant", x, y, 50)
            powerups.insert(i, carb)

        i = 0
        while i < 3: # 2 gazbottle
            i += 1
            x = int(random.random() * 1000)
            y = int(-random.random() * 1000)
            objet = Objet("bouteille", x, y)
            powerups.insert(i, objet)


        return powerups


if __name__ == '__main__':
    print(int(-random.random()*1000))