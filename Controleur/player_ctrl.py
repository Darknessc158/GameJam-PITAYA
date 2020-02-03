from Model.player import Player
import pygame
from pygame.locals import *
# A faire : fuel qui diminue score, altitude qui augmente temps qui augmente obstacles qui bloque ou tue le joueur
# Objet supplementaire : haricot magique , aile , pitaya ...

# Creation d'un joueur au centre de la map
player1 = Player(1, int(1024/2)-40, int(768/2)-40, 100)
player_position = (player1.get_x(), player1.get_y())


# Test des evenements
pygame.init()
screen = pygame.display.set_mode((1024, 768), RESIZABLE)
# fond et collage du fond à la fenetre
fond = pygame.Surface(screen.get_size())
fond.fill((100,100,200))
# fond = pygame.image.load("../model/data/background.jpg").convert()
screen.blit(fond, (0, 0))
# Chargement et collage du personnage
perso = pygame.image.load("../model/data/perso.png").convert_alpha() #convert alpha pour la transparance du png
screen.blit(perso, player_position)


# Boucle affichage de la fenetre
## ici variables pour retenir en mémoire l’état des touches
droite = False
gauche = False
jump = False
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            ## on met a True l’état quand on appuye sur la touche
            if event.key == pygame.K_RIGHT:
                droite = True
            elif event.key == pygame.K_LEFT:
                gauche = True
            elif event.key == pygame.K_SPACE:
                jump = True
        elif event.type == pygame.KEYUP:
            ## on met a False l’état quand la touche est relâchée
            if event.key == pygame.K_RIGHT:
                droite = False
            elif event.key == pygame.K_LEFT:
                gauche = False
            elif event.key == pygame.K_SPACE:
                jump = False
    ## et on traite les évènements ici
    if droite:
        player_position = player1.movePositCourante(1, 0)
    elif gauche:
        player_position = player1.movePositCourante(-1, 0)
    elif jump:
        player_position = player1.movePositCourante(0, -1)
    #à supprimer juste pour get la position du pointeur
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
        print(pygame.mouse.get_pos())  # getposition

    # Re-collage
    screen.blit(fond, (0, 0))
    screen.blit(perso, player_position)
    # Rafraichissement
    pygame.display.flip()


