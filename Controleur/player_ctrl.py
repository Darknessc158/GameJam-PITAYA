#Import
import sys
sys.path.append('../GameJam-PITAYA/View')
sys.path.append('../GameJam-PITAYA/Model')


from Model.player import Player

import pygame
from Model.game import Game
from Model.objet import Ennemi
from pygame.locals import *


from Model.plateformedisplay import Plateformedisplay
from Model.objet import Objet
from Model.objet import Carburant

import time

# A faire :
# Objet supplementaire : haricot magique , aile , pitaya ...

# Creation d'un joueur au centre de la map
player1 = Player(1, int(1024/2)-40, int(768/2)-40, 100)
player_position = (player1.get_x(), player1.get_y())
quantitefuel = player1.get_fuel()

#Creation d'une game
game1 = Game(0, 0) #score et time
#Creation plateforme
plateformes = game1.generatePlateformes().copy()
#Creation objet
powerups = game1.generate_objet().copy()

# Test des evenements
pygame.init()
screen = pygame.display.set_mode((1024, 768), RESIZABLE)
# fond et collage du fond à la fenetre
fond = pygame.Surface(screen.get_size())
#fond.fill((100,100,200))
fond = pygame.image.load("../Model/data/map_background.png").convert()
screen.blit(fond, (0, -9000))
# Chargement et collage du personnage
# convert alpha pour la transparance du png

perso = pygame.image.load("../Model/data/cosmonaut-idle-100.png")
screen.blit(perso, player_position)

pygame.display.flip()


# Boucle affichage de la fenetre
## ici variables pour retenir en mémoire l’état des touches
droite = False
gauche = False
haut = False
bas = False
fall = True
boost = False
fuelHit = False
niveauFall = 0
fallspeed = 1
timefuel = 0
defilmap = -9000
launched = True
powerup = False
estSurPlateforme = False

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            ## on met a True l’état quand on appuie sur la touche
            if event.key == pygame.K_RIGHT:
                droite = True
                if min_xplat <= max_x and min_x <= max_xplat and (max_yplat - 5) <= min_y <= (max_yplat + 5):
                    fall = False
                if estSurPlateforme == False:
                    fall = True
            elif event.key == pygame.K_LEFT:
                gauche = True
                if estSurPlateforme == False:
                    fall = True
            elif event.key == pygame.K_UP:
                perso = pygame.image.load("../Model/data/cosmonaut-jump-100.png")
                screen.blit(perso, player_position)
                haut = True
                fall = True
            elif event.key == pygame.K_DOWN:
                bas = True
                fall = True
            elif event.key != pygame.K_DOWN:
                fall = True
        elif event.type == pygame.KEYUP:
            ## on met a False l’état quand la touche est relâchée
            if event.key == pygame.K_RIGHT:
                droite = False
                fall = True
            elif event.key == pygame.K_LEFT:
                gauche = False
                fall = True
            elif event.key == pygame.K_UP:
                haut = False
                fall = True
            elif event.key == pygame.K_DOWN:
                bas = False
                fall = True



    #Gestion deplacement bord de l'ecran
    if player1.get_x() >= 940:
        droite=False
    elif player1.get_x() <=5:
        gauche=False
    elif player1.get_y() >= 700:
        launched=False
    elif player1.get_y() <= 7:
        haut=False


    ## et on traite les évènements ici
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

        if min_xplat <= max_x and min_x <= max_xplat and powerup == False:  # Est sur la longueur de la plateforme
            if (max_yplat - 5) <= min_y <= (max_yplat + 5):  # collisation par le bas
                if plateforme.get_type() == 'teleportation':
                    player_position = player1.movePositTeleportation()
                haut = False
                # player_position = player1.movePositCourante(0, fallspeed)
                # fall = False
            if (min_yplat - 5) <= max_y <= (min_yplat + 5):  # colisation par en haut
                if plateforme.get_type() == 'poison':
                    launched = False
                elif plateforme.get_type() == 'teleportation':
                    player_position = player1.movePositTeleportation()
                elif plateforme.get_type() == 'CarburantMoins':
                    player1.remove_fuel()
                    fuelHit = True
                bas = False
                player_position = player1.movePositCourante(0, fallspeed) #descends à la vitesse des plateformes
                fall = False
                # Recharge le fuel si le player est posé sur une plateforme
                player1.add_fuel(0.2)
                quantitefuel = int(player1.get_fuel())
                #Mets l'image de marche
                perso = pygame.image.load("../Model/data/cosmonaut-march-100.png")
        if min_y <= min_yplat and max_y >= max_yplat:  # Est sur la largeur de la plateforme
                estSurPlateforme = True
        else:
            estSurPlateforme = False
        if min_y <= min_yplat and max_y >= max_yplat and powerup == False:  # Est sur la largeur de la plateforme
            if (max_xplat - 5) <= min_x <= (max_xplat + 5):  # collision par la droite (petite marge pour eviter les bug de traversement)
                gauche = False
            if (min_xplat - 5) <= max_x <= (min_xplat + 5):  # collision par la gauche
                droite = False

    #Gestion des bords
    if droite:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(2, 0)
            player_position = player1.movePositCourante(0, 0.5)
    elif gauche:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(-2, 0)
            player_position = player1.movePositCourante(0, 0.5)
    elif haut:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(0, -5)

    ## et on traite les évènements ici
    if droite:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(1, 0)
            # player_position = player1.movePositCourante(0, 1.5)
    elif gauche:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(-1, 0)
            # player_position = player1.movePositCourante(0, 1.5)
    elif haut:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(0, -1.5)
    elif fall:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            if niveauFall == 0 :
                player_position = player1.movePositCourante(0, 1.5)
            elif niveauFall == 1:
                player_position = player1.movePositCourante(0, 1.75)
            elif  niveauFall == 2:
                 player_position = player1.movePositCourante(0, 2)
            elif niveauFall == 3:
                player_position = player1.movePositCourante(0, 2.25)
            elif niveauFall == 4:
                player_position = player1.movePositCourante(0, 2.50)
            elif niveauFall == 5:
                player_position = player1.movePositCourante(0, 2.75)
            elif niveauFall == 6:
                player_position = player1.movePositCourante(0, 3)
            elif niveauFall == 7:
                player_position = player1.movePositCourante(0, 3.25)
            elif niveauFall == 8:
                player_position = player1.movePositCourante(0, 3.50)
            elif niveauFall > 8:
                player_position = player1.movePositCourante(0, 5)


    # Re-collage
    defilmap += 1 #defilement de la map
    screen.blit(fond, (0, defilmap))
    if defilmap == 0:
        screen.fill((0, 0, 0))
    screen.blit(perso, player_position)

    # Fuel
    timefuel += 1
    if (timefuel % 20) == 0: #Retourne la duree depuis que pygame.init a été appeler en ms
        quantitefuel -= 1 #diminue de 1 le fuel à chaque boucle modulo 10 du timefuel
        player1.set_fuel(quantitefuel)
    if quantitefuel <= 0:
        launched = False
    rect = pygame.Rect(740, 677, quantitefuel*2, 25)
    pygame.draw.rect(screen, (255, 0, 0), rect)
    text = pygame.font.Font('freesansbold.ttf', 20)
    fuel = text.render('Carburant : {}'.format(int(player1.get_fuel())), True, (0, 0, 0))
    screen.blit(fuel, (750, 680))

    #Fuel reduit alert
    if fuelHit == True:
        text = pygame.font.Font('freesansbold.ttf', 55)
        carb = text.render('-75', True, (255, 0, 0))
        screen.blit(carb, (900, 625))
        fuelHit = False

    # Message alerte fuel
    if player1.get_fuel() <= 30:
        text = pygame.font.Font('freesansbold.ttf', 25)
        carb = text.render('Alerte ! Alerte ! Niveau carburant bas', True, (255, 0, 0))
        screen.blit(carb, (325, 200))

    #Score
    game1.set_time(timefuel)
    if (game1.get_time() % 50) == 0:
        game1.add_score(1)
    text = pygame.font.Font('freesansbold.ttf', 50)
    score = text.render('Score : {}'.format(game1.get_score()), True, (0, 0, 0))
    screen.blit(score, (20, 20))

    # Plateformes
    for plateforme in plateformes: #collage des plateformes
        rect = pygame.Rect(int(plateforme.get_x()), int(plateforme.get_y()), int(plateforme.get_long()), int(plateforme.get_larg()))
        if(plateforme.get_type() == 'poison'):
            pygame.draw.rect(screen, (0, 255, 0), rect)
        elif(plateforme.get_type() == 'teleportation'):
            pygame.draw.rect(screen, (0, 191, 255), rect)
        elif(plateforme.get_type() == 'CarburantMoins'):
            pygame.draw.rect(screen, (255,255,0), rect)
        else:
            pygame.draw.rect(screen, (105, 105, 105), rect)

    for plateforme in plateformes: #Chute des plateformes pour la prochaine boucle
        plateforme.set_position(0, fallspeed)
    screen.blit(perso, player_position)
    #Power up
    for objet in powerups: # Chute des objets
        objet.set_position(0, fallspeed)
    for objet in powerups:
        if (objet.get_name() == "carburant"):
            pygame.draw.circle(screen, (255, 0, 0), (objet.get_x(), objet.get_y()), 20)
        elif (objet.get_name() == "bouteille"):
            pygame.draw.circle(screen, (128, 128, 128), (objet.get_x(), objet.get_y()), 20)

        # Verif si le player est sur le power up
        #surface de l'objet
        min_yobj = int(objet.get_y() - 20) # 20 == rayon du cercle
        max_yobj = int(objet.get_y() + 20)
        min_xobj = int(objet.get_x() - 20)
        max_xobj = int(objet.get_x() + 20)

        # recalcul surface de l'image du player
        min_x = int(player1.get_x())
        max_x = int(player1.get_x() + 100)
        min_y = int(player1.get_y())
        max_y = int(player1.get_y() + 100)
        if min_yobj <= max_y and max_yobj >= min_y: #sur la largeur de l'objet
            if min_xobj <= max_x and max_xobj >= min_x: #Sur la longueur de l'objet
                # print("L'astronaute est sur l'objet")
                if (objet.get_name() == "carburant"):
                    player1.add_fuel(objet.get_quantite())
                    quantitefuel = player1.get_fuel()

                if (objet.get_name() == "bouteille"):
                    fallspeed = fallspeed + 4
                    powerup = True
                    game1.add_score(40)
                    powerups.remove(objet)
                    haut = True
                    fall = False

    if (timefuel % 500) == 0 and powerup == True:  # On remet la vitesse normal apres le power up
        fallspeed = fallspeed - 4
        powerup = False
        fall = True

    if (timefuel % 500) == 0:  # Difficulte augmente
        fallspeed = fallspeed + 0.25
        niveauFall += 1
        print(niveauFall)
        powerup = False


    # Rafraichissement
    pygame.display.flip()

    # à supprimer juste pour get la position du pointeur
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
        print(pygame.mouse.get_pos())  # getposition
