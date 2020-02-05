import sys
sys.path.append('../GameJam-PITAYA/View')
sys.path.append('../GameJam-PITAYA/Model')

from player import Player
import pygame
from game import Game
from objet import Ennemi
from pygame.locals import *
from plateformedisplay import Plateformedisplay
# A faire : obstacles qui bloque ou tue le joueur
# Objet supplementaire : haricot magique , aile , pitaya ...

# Creation d'un joueur au centre de la map
player1 = Player(1, int(1024/2)-40, int(768/2)-40, 100)
player_position = (player1.get_x(), player1.get_y())
player_position2 = (player1.get_x()-50, player1.get_y()-50)
quantitefuel = player1.get_fuel()
#Creation d'une game
game1 = Game(0, 0) #score et time
#Creation plateforme
plateforme1 = Plateformedisplay(300, 50, 200, 10, 'normal') # x y long larg type
plateforme2 = Plateformedisplay(700, 50, 200, 10, 'normal')
plateforme3 = Plateformedisplay(450, 200, 200, 10, 'normal')
plateforme4 = Plateformedisplay(15, 250, 200, 10, 'normal')
plateforme5 = Plateformedisplay(300, -100, 200, 10, 'normal') # x y long larg type
plateforme6 = Plateformedisplay(700, -300, 200, 10, 'normal')
plateforme7 = Plateformedisplay(450, -500, 200, 10, 'normal')
plateforme8 = Plateformedisplay(15, -200, 200, 10, 'normal')
plateformes = [plateforme1, plateforme2, plateforme3, plateforme4, plateforme5, plateforme6, plateforme7, plateforme8]

# Test des evenements
pygame.init()
screen = pygame.display.set_mode((1024, 768), RESIZABLE)
# fond et collage du fond à la fenetre
fond = pygame.Surface(screen.get_size())
fond.fill((100,100,200))
# fond = pygame.image.load("../model/data/background.jpg").convert()
screen.blit(fond, (0, 0))
# Chargement et collage du personnage
# convert alpha pour la transparance du png
perso = pygame.image.load("/home/darknessc158/IUT/GameJam/GameJam-PITAYA/Model/data/perso.png").convert_alpha()
screen.blit(perso, player_position)
perso2 = pygame.image.load("/home/darknessc158/IUT/GameJam/GameJam-PITAYA/Model/data/perso.png").convert_alpha()
screen.blit(perso2, player_position2)


# Boucle affichage de la fenetre
## ici variables pour retenir en mémoire l’état des touches
droite = False
gauche = False
haut = False
bas = False
fall = True
timefuel = 0
launched = True
collision=False
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            ## on met a True l’état quand on appuie sur la touche
            if event.key == pygame.K_RIGHT:
                if player1.get_x() <= 1024:
                    droite = True
            elif event.key == pygame.K_LEFT:
                gauche = True
            elif event.key == pygame.K_UP:
                haut = True
            elif event.key == pygame.K_DOWN:
                bas = True
            elif event.key != pygame.K_DOWN:
                fall = True
        elif event.type == pygame.KEYUP:
            ## on met a False l’état quand la touche est relâchée
            if event.key == pygame.K_RIGHT:
                droite = False
            elif event.key == pygame.K_LEFT:
                gauche = False
            elif event.key == pygame.K_UP:
                haut = False
            elif event.key == pygame.K_DOWN:
                bas = False

    #Gestion deplacement bord de l'ecran
    if player1.get_x() >= 940:
        droite=False
    elif player1.get_x()  <=10:
        gauche=False
    elif player1.get_y() >= 700:
        launched=False
    elif player1.get_y() <= 7:
        haut=False

    # Gestion collision player-plateformes

    # surface de l'image du player
    min_x = int(player1.get_x())
    max_x = int(player1.get_x() + 100)
    min_y = int(player1.get_y())
    max_y = int(player1.get_y() + 100)

    for plateforme in plateformes:
        # surface de la plateforme courante
        min_xplat = int(plateforme.get_x())
        max_xplat = int(plateforme.get_x() + plateforme.get_long())
        min_yplat = int(plateforme.get_y())
        max_yplat = int(plateforme.get_y() + plateforme.get_larg())

        if min_xplat <= max_x and min_x <= max_xplat:  # Est sur la longueur de la plateforme
            if max_y == min_yplat:  # colisation par en haut
                bas = False
            if min_y == max_yplat:  # collisation par le bas
                haut = False
        if min_y <= min_yplat and max_y >= max_yplat:  # Est sur la largeur de la plateforme
            if (max_xplat - 5) <= min_x <= (max_xplat + 5):  # collision par la droite (petite marge pour eviter les bug de traversement)
                gauche = False
            if (min_xplat - 5) <= max_x <= (min_xplat + 5):  # collision par la gauche
                droite = False
        if pygame.Rect(player1.get_x(), player1.get_y(), 100, 100).colliderect(plateforme.get_x(),plateforme.get_y(),plateforme.get_larg(),plateforme.get_long()):
            collision=True
        else:
            collision=False
    ## et on traite les évènements ici
    if droite:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(1, 0)
            player_position = player1.movePositCourante(0, 1.5)
    elif gauche:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(-1, 0)
            player_position = player1.movePositCourante(0, 1.5)
    elif haut:
       if collision == False:
            if player1.get_x() >= 0 or player1.get_x() <= 1024:
                player_position = player1.movePositCourante(0, -1.5)
    elif bas:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(0, 2)
    elif fall:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(0, 1.5)


    # Re-collage
    screen.blit(fond, (0, 0))
    screen.blit(perso, player_position)
    #screen.blit(perso2, player_position2)

    # Fuel
    timefuel += 1
    if (timefuel % 150) == 0: #Retourne la duree depuis que pygame.init a été appeler en ms
        quantitefuel -= 1 #diminue de 1 le fuel à chaque boucle modulo 10 du timefuel
        player1.set_fuel(quantitefuel)
    if quantitefuel <= 0:
        launched = False
    rect = pygame.Rect(740, 690, quantitefuel*2, 25)
    pygame.draw.rect(screen, (255, 0, 0), rect)
    text = pygame.font.Font('freesansbold.ttf', 20)
    fuel = text.render('Carburant : {}'.format(player1.get_fuel()), True, (0, 0, 0))
    screen.blit(fuel, (750, 693))
    #Score
    game1.set_time(timefuel)
    if (game1.get_time() % 50) == 0:
        game1.add_score(1)
    text = pygame.font.Font('freesansbold.ttf', 25)
    score = text.render('Score : {}'.format(game1.get_score()), True, (0, 0, 0))
    screen.blit(score, (20, 20))

    # Plateformes
    for plateforme in plateformes: #collage des plateformes
        rect = pygame.Rect(int(plateforme.get_x()), int(plateforme.get_y()), int(plateforme.get_long()), int(plateforme.get_larg()))
        pygame.draw.rect(screen, (0, 255, 0), rect)

    for plateforme in plateformes: #Chute des plateformes pour la prochaine boucle
        plateforme.set_position(0, 0.8)

    # Rafraichissement
    pygame.display.flip()

    # à supprimer juste pour get la position du pointeur
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
        print(pygame.mouse.get_pos())  # getposition
