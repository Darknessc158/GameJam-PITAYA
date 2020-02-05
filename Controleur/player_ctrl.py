#Import
import sys
sys.path.append('../GameJam-PITAYA/View')
sys.path.append('../GameJam-PITAYA/Model')
from Model.player import Player
from Model.game import Game
import pygame
from pygame.locals import *
import time

# Creation d'un joueur au centre de la map
player1 = Player(1, int(1024/2)-40, int(768/2)-40, 100)
player_position = (player1.get_x(), player1.get_y())
quantitefuel = player1.get_fuel()

#Creation d'une game
game1 = Game(0, 0)# score et time
#Creation plateforme
plateformes = game1.generatePlateformes()
#Creation objet
powerups = game1.generate_objet()

# Test des evenements
pygame.init()
screen = pygame.display.set_mode((1024, 768), RESIZABLE)

# Background
fond = pygame.image.load("../Model/data/map_background.png").convert() #map jusqu'a 10000px
defilmap = -9000
# Chargement et collage du personnage
# convert alpha pour la transparance du png
perso = pygame.image.load("../Model/data/cosmonaut-idle-100.png") #image du perso de base

## ici variables pour retenir en mémoire l’état des touches

#variable deplacement
droite = False
gauche = False
haut = False
bas = False

listekeypressed = []

fall = True # de base le perso chute
fallspeed = 2

#timeinsecond = int(time.time() % 60)

timefuel = 0
nbboucle = 0
boucle = 0

launched = True
powerup = False #powerup actif ou non
estSurPlateforme = False

while launched:
    fall = True  # Pour le faire rechuter quand il quitte la plateforme
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN: #Si une touche est enfoncée
            listekeypressed.append(event.key) #insertion des touches enfoncées dans la liste
            if pygame.K_RIGHT in listekeypressed:
                #Sprite droit
                droite = True
            elif pygame.K_LEFT in listekeypressed:
                perso = pygame.image.load("../Model/data/cosmonaut-idle2-100.png")
                gauche = True
            if pygame.K_UP in listekeypressed:
                perso = pygame.image.load("../Model/data/cosmonaut-jump-100.png")
                haut = True
            elif pygame.K_DOWN in listekeypressed:
                perso = pygame.image.load("../Model/data/cosmonaut-jump-100.png")
                bas = True

        elif event.type == pygame.KEYUP: #Si une touche est relachée
            listekeypressed.remove(event.key)## supression de la touche relâchée
            if event.key == pygame.K_RIGHT:
                droite = False
            elif event.key == pygame.K_LEFT:
                gauche = False
            elif event.key == pygame.K_UP:
                haut = False
            elif event.key == pygame.K_DOWN:
                bas = False

    # calcul de la surface de l'image du player
    min_x = int(player1.get_x())
    max_x = int(player1.get_x() + 100)
    min_y = int(player1.get_y())
    max_y = int(player1.get_y() + 100)

    #Gestion des bords de l'ecran
    # Droite / Gauche
    if max_x >= 1060:
        droite = False
    elif min_x <= 0:
        gauche = False
    # Haut / Bas
    if min_y <= 5:
        haut = False
    elif max_y >= 768:
        launched = False


    # Gestion collision player-plateformes

    for plateforme in plateformes:
        # surface de la plateforme courante
        min_xplat = int(plateforme.get_x())
        max_xplat = int(plateforme.get_x() + plateforme.get_long())
        min_yplat = int(plateforme.get_y())
        max_yplat = int(plateforme.get_y() + plateforme.get_larg())

        if min_xplat <= max_x and min_x <= max_xplat and powerup == False:  # Est sur la longueur de la plateforme
            if (max_yplat - 5) <= min_y <= (max_yplat + 5):  # collision par le bas
                haut = False
                player_position = player1.movePositCourante(0, fallspeed)  # descends à la vitesse des plateformes
                if plateforme.get_type() == 'teleportation':
                    player_position = player1.movePositTeleportation()
            if (min_yplat - 5) <= max_y <= (min_yplat + 5):  # collision par le haut
                bas = False
                fall = False
                player_position = player1.movePositCourante(0, fallspeed)  # descends à la vitesse des plateformes
                # Rechargement du fuel
                player1.add_fuel(0.2)
                quantitefuel = int(player1.get_fuel())
                # Mets l'image de pose
                perso = pygame.image.load("../Model/data/Cosmonaut-march-100.png")
                #Action des plateformes
                if plateforme.get_type() == 'poison':
                    launched = False
                elif plateforme.get_type() == 'teleportation':
                    player_position = player1.movePositTeleportation()

        if min_y <= min_yplat and max_y >= max_yplat and powerup == False:  # Est sur la largeur de la plateforme
            if (max_xplat - 5) <= min_x <= (max_xplat + 5):  # collision par la droite (petite marge pour eviter les bug de traversement)
                gauche = False
            if (min_xplat - 5) <= max_x <= (min_xplat + 5):  # collision par la gauche
                droite = False

        if min_y <= min_yplat and max_y >= max_yplat and powerup == False and min_xplat <= max_x and min_x <= max_xplat and powerup == False:# Il est sur une plateforme
            fall = False

    # Re-collage du fond et du player
    defilmap += 1  # defilement de la map
    screen.blit(fond, (0, defilmap))  # recollage map


    # Fuel
    timefuel += 1
    if (timefuel % 20) == 0: #Retourne la duree depuis que pygame.init a été appeler en ms
        quantitefuel -= 1 #diminue de 1 le fuel à chaque boucle modulo 20 du timefuel
        player1.set_fuel(quantitefuel)
    if quantitefuel <= 0:
        launched = False
    # Dessin et collage du carburant
    rect = pygame.Rect(740, 690, quantitefuel*2, 25)
    pygame.draw.rect(screen, (255, 0, 0), rect)
    text = pygame.font.Font('freesansbold.ttf', 20)
    fuel = text.render('Carburant : {}'.format(int(player1.get_fuel())), True, (0, 0, 0))
    screen.blit(fuel, (750, 693))
    # Message alerte fuel
    if player1.get_fuel() <= 30:
        text = pygame.font.Font('freesansbold.ttf', 15)
        carb = text.render('Alerte ! Alerte ! Niveau carburant bas', True, (255, 0, 0))
        screen.blit(carb, (400, 200))


    # Score
    game1.set_time(int(pygame.time.get_ticks()/1000)) #time in ms depuis pygame.init()
    if (timefuel % 50) == 0:# ajout de score vitesse de base
        game1.add_score(1)
    text = pygame.font.Font('freesansbold.ttf', 25)
    text2 = pygame.font.Font('freesansbold.ttf', 15)
    score = text.render('Score : {}'.format(game1.get_score()), True, (0, 0, 0))
    time = text2.render('Temps : {} secondes'.format(game1.get_time()), True, (0, 0, 0))
    screen.blit(score, (20, 20))
    screen.blit(time, (20, 60))


    # Collage des plateformes sur l'ecran
    for plateforme in plateformes:
        rect = pygame.Rect(int(plateforme.get_x()), int(plateforme.get_y()), int(plateforme.get_long()), int(plateforme.get_larg()))
        if(plateforme.get_type() == 'poison'):
            pygame.draw.rect(screen, (0, 255, 0), rect)
        elif(plateforme.get_type() == 'teleportation'):
            pygame.draw.rect(screen, (0, 191, 255), rect)
        else:
            pygame.draw.rect(screen, (105, 105, 105), rect)
        plateforme.set_position(0, fallspeed)


    #Power up
    for objet in powerups:
        if (objet.get_name() == "carburant"):
            pygame.draw.circle(screen, (255, 0, 0), (objet.get_x(), objet.get_y()), 20)
        elif (objet.get_name() == "bouteille"):
            pygame.draw.circle(screen, (128, 128, 128), (objet.get_x(), objet.get_y()), 20)
        objet.set_position(0, fallspeed)
        # Verif si le player est sur le power up
        #surface de l'objet
        min_yobj = int(objet.get_y() - 20) # 20 == rayon du cercle
        max_yobj = int(objet.get_y() + 20)
        min_xobj = int(objet.get_x() - 20)
        max_xobj = int(objet.get_x() + 20)
        if min_yobj <= max_y and max_yobj >= min_y: #sur la largeur de l'objet
            if min_xobj <= max_x and max_xobj >= min_x: #Sur la longueur de l'objet
                # L'astronaute est sur l'objet
                if (objet.get_name() == "carburant"): #Action des powerups
                    player1.add_fuel(objet.get_quantite())
                    quantitefuel = player1.get_fuel()
                if (objet.get_name() == "bouteille"):
                    fallspeed = 4
                    powerup = True
                    game1.add_score(40)
                    nbboucle = boucle
                powerups.remove(objet)
    #Desactivation de l'effet du powerup
    if nbboucle <= (boucle-150) and powerup == True:  # On remet la vitesse normal apres 200 boucles
        fallspeed = 2
        powerup = False


    ## Traitement des deplacements
    # Droite / Gauche
    if droite:
            player_position = player1.movePositCourante(6, 0)
            player_position = player1.movePositCourante(0, 1.5)# chute
    elif gauche:
            player_position = player1.movePositCourante(-6, 0)
            player_position = player1.movePositCourante(0, 1.5)# chute
    # Haut / Bas
    if haut:
            player_position = player1.movePositCourante(0, -10)
    elif bas:
            player_position = player1.movePositCourante(0, 5)
    # Chute
    if fall:
        player_position = player1.movePositCourante(0, 3.5)


    # recollage du pers
    screen.blit(perso, player_position)


    # Rafraichissement
    pygame.display.flip()

    boucle += 1

