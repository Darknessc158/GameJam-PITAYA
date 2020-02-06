import sys
sys.path.append('../GameJam-PITAYA/View')
import pygame
import random
from Model.plateformedisplay import Plateformedisplay
from pygame.locals import *
from Model.objet import Objet
from Model.objet import Carburant
import random
import time


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
                yrand = random.randrange(-8500, -4500, 150)
                randlong = random.choice(long)
            elif counter >= 150 and counter < 200:
                xrand = random.choice(x_default)
                yrand = random.randrange(-16500, -8500, 225)
                randlong = random.choice(long)
            elif counter >= 200 and counter < 250:
                xrand = random.choice(x_default)
                yrand = random.randrange(-24500, -16500, 335)
                randlong = random.choice(long)
            elif counter >= 250 and counter < 300:
                xrand = random.choice(x_default)
                yrand = random.randrange(-32500, -24500, 350)
                randlong = random.choice(long)
            elif counter >= 300 and counter < 350:
                xrand = random.choice(x_default)
                yrand = random.randrange(-40500, -32500, 150)
                randlong = random.choice(long)
            elif counter >= 350 and counter < 400:
                xrand = random.choice(x_default)
                yrand = random.randrange(-48500, -40500, 75)
                randlong = random.choice(long)
            elif counter >= 400 and counter < 450:
                xrand = random.choice(x_default)
                yrand = random.randrange(-56500, -48500, 100)
                randlong = random.choice(long)
            elif counter >= 450 and counter <= 500:
                xrand = random.choice(x_default)
                yrand = random.randrange(-64500, -56500, 50)
                randlong = random.choice(long)

            if counter % 69 == 0:
                plateforme = Plateformedisplay(xrand, yrand, randlong, 10, 'poison')
            elif counter % 30 == 0:
                plateforme =  Plateformedisplay(xrand, yrand, randlong, 10, 'teleportation')
            elif counter % 10 == 0:
                plateforme = Plateformedisplay(xrand, yrand, randlong, 10, 'CarburantMoins')
            else:
                plateforme= Plateformedisplay(xrand, yrand, randlong, 10, 'normal')
            plateformes.append(plateforme)
            counter += 1

        return plateformes

    def generate_objet(self):
        counter = 0
        x_default = [300, 450, 350, 500, 650, 400, 700, 200, 50, 600, 100, 900, 850]
        powerups = []
        while counter < 150:
            if counter < 10:
                xrand = random.choice(x_default)
                yrand = random.randrange(-4500, 700, 200)
            elif counter >= 10 and counter < 20:
                xrand = random.choice(x_default)
                yrand = random.randrange(-8500, -4500, 450)
            elif counter >= 20 and counter < 30:
                xrand = random.choice(x_default)
                yrand = random.randrange(-16500, -8500, 500)
            elif counter >= 40 and counter < 50:
                xrand = random.choice(x_default)
                yrand = random.randrange(-24500, -16500, 650)
            elif counter >= 50 and counter < 60:
                xrand = random.choice(x_default)
                yrand = random.randrange(-32500, -24500, 750)
            elif counter >= 60 and counter < 80:
                xrand = random.choice(x_default)
                yrand = random.randrange(-40500, -32500, 775)
            elif counter >= 80 and counter < 100:
                xrand = random.choice(x_default)
                yrand = random.randrange(-48500, -40500, 850)
            elif counter >= 120 and counter < 140:
                xrand = random.choice(x_default)
                yrand = random.randrange(-56500, -48500, 900)
            elif counter >= 140 and counter <= 150:
                xrand = random.choice(x_default)
                yrand = random.randrange(-64500, -56500, 8000)

            if counter % 5 == 0:
                objet = Objet("bouteille",xrand, yrand)
            else:
                objet = Carburant("carburant", xrand, yrand, 50)
            powerups.append(objet)
            counter += 1

        return powerups

    def get_diffculty_set(self):
        file_difficulty = open("../Model/highscore.txt", "r")
        difficulty = int(file_difficulty.readline())
        return difficulty



if __name__ == '__main__':
    t = int((time.time() % 60))
    print((int((time.time() % 60)) - t))