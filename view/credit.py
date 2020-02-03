import pygame
from pygame.locals import *

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

#screen parameters
pygame.init()
screen = pygame.display.set_mode((1024, 768), RESIZABLE)

#credits text

title = pygame.font.Font('freesansbold.ttf', 25)
credit = title.render('Credits', True, white)
dev = title.render('Developpeurs :', True, white)
des = title.render('Designer :', True, white)

name = pygame.font.Font('freesansbold.ttf', 16)
remi = name.render('CHEN Rémi', True, white)
aure = name.render('BERNABE Aurélien', True, white)
naod = name.render('BEKELE Naod', True, white)
arthur = name.render('PARDIEU Arthur', True, white)
#Boucle infinie pour garder la fenetre
launched = True
while launched:
    screen.blit(credit, (435, 10))

    screen.blit(dev, (50, 100))
    screen.blit(remi, (50, 140))
    screen.blit(aure, (50, 160))
    screen.blit(naod, (50, 180))

    screen.blit(des, (50, 290))
    screen.blit(arthur, (50, 330))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == KEYDOWN:
            print(pygame.mouse.get_pos())
    # Rafraichissement
    pygame.display.flip()