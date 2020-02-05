import sys
sys.path.append('../GameJam-PITAYA/View')
import pygame
import random
from Model.plateformedisplay import Plateformedisplay
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

    def generatePlateformes(self):
        counter=0
        x_default = [300,450, 350, 500, 650, 400, 700, 200, 50, 600, 100]
        long = [ 50, 150,  100]
        plateformes=[]
        while counter < 500:
            if counter < 50:
                xrand = random.choice(x_default)
                yrand = random.randrange(-4500, 700, 100)
                randlong = random.choice(long)
            elif counter >= 50 and counter <100:
                xrand = random.choice(x_default)
                yrand = random.randrange(-8500, -4500, 250)
                randlong = random.choice(long)
            elif counter >= 150 and counter < 200:
                xrand = random.choice(x_default)
                yrand = random.randrange(-16500, -8500, 350)
                randlong = random.choice(long)
            elif counter >= 200 and counter < 250:
                xrand = random.choice(x_default)
                yrand = random.randrange(-24500, -16500, 450)
                randlong = random.choice(long)
            elif counter >= 250 and counter < 300:
                xrand = random.choice(x_default)
                yrand = random.randrange(-32500, -24500, 550)
                randlong = random.choice(long)
            elif counter >= 300 and counter < 350:
                xrand = random.choice(x_default)
                yrand = random.randrange(-40500, -32500, 650)
                randlong = random.choice(long)
            elif counter >= 350 and counter < 400:
                xrand = random.choice(x_default)
                yrand = random.randrange(-48500, -40500, 750)
                randlong = random.choice(long)
            elif counter >= 400 and counter < 450:
                xrand = random.choice(x_default)
                yrand = random.randrange(-56500, -48500, 850)
                randlong = random.choice(long)
            elif counter >= 450 and counter <= 500:
                xrand = random.choice(x_default)
                yrand = random.randrange(-64500, -56500, 950)
                randlong = random.choice(long)

            if counter % 3 == 0:
                plateforme = Plateformedisplay(xrand, yrand, randlong, 10, 'poison')
            else:
                plateforme= Plateformedisplay(xrand, yrand, randlong, 10, 'normal')
            plateformes.append(plateforme)
            counter += 1

        return plateformes

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