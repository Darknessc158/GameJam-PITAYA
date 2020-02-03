import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024, 768), RESIZABLE)

# fond et collage du fond à la fenetre
fond = pygame.image.load("../model/data/background.jpg").convert()
screen.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("../model/data/perso.png").convert_alpha() #convert alpha pour la transparance du png
position_perso = perso.get_rect()
screen.blit(perso, position_perso)

#Boucle infinie pour garder la fenetre
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_perso = position_perso.move(0, 10)
            if event.key == K_UP:
                position_perso = position_perso.move(0, -10)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-10, 0)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(10, 0)

    # Re-collage
    screen.blit(fond, (0, 0))
    screen.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()