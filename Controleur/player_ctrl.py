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
plateforme1 = Plateformedisplay(300, 50, 200, 10, 'normal') # x y long larg type
plateforme2 = Plateformedisplay(700, 50, 200, 10, 'normal')
plateforme3 = Plateformedisplay(450, 200, 200, 10, 'normal')
plateforme4 = Plateformedisplay(15, 250, 200, 10, 'normal')
plateforme5 = Plateformedisplay(300, -100, 200, 10, 'normal') # x y long larg type
plateforme6 = Plateformedisplay(700, -300, 200, 10, 'normal')
plateforme7 = Plateformedisplay(450, -500, 200, 10, 'normal')
plateforme8 = Plateformedisplay(15, -200, 200, 10, 'normal')
plateformes = [plateforme1, plateforme2, plateforme3, plateforme4, plateforme5, plateforme6, plateforme7, plateforme8]

#Creation objet
powerups = game1.generate_objet()

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
perso = pygame.image.load("../Model/data/perso.png").convert_alpha()
screen.blit(perso, player_position)
#perso2 = pygame.image.load("../Model/data/perso.png").convert_alpha()
#screen.blit(perso2, player_position2)


# Boucle affichage de la fenetre
## ici variables pour retenir en mémoire l’état des touches
droite = False
gauche = False
haut = False
bas = False
fall = True
fallspeed = 0.5
timefuel = 0
launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            ## on met a True l’état quand on appuie sur la touche
            if event.key == pygame.K_RIGHT:
                droite = True
                fall = True
            elif event.key == pygame.K_LEFT:
                gauche = True
                fall = True
            elif event.key == pygame.K_UP:
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
    elif player1.get_x()  <=10:
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

        if min_xplat <= max_x and min_x <= max_xplat:  # Est sur la longueur de la plateforme
            if (max_yplat - 5) <= min_y <= (max_yplat + 5):  # collisation par le bas
                haut = False
                # player_position = player1.movePositCourante(0, fallspeed)
                # fall = False
            if (min_yplat - 5) <= max_y <= (min_yplat + 5):  # colisation par en haut
                bas = False
                player_position = player1.movePositCourante(0, fallspeed)
                fall = False
        if min_y <= min_yplat and max_y >= max_yplat:  # Est sur la largeur de la plateforme
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
    if (timefuel % 20) == 0: #Retourne la duree depuis que pygame.init a été appeler en ms
        quantitefuel -= 1 #diminue de 1 le fuel à chaque boucle modulo 10 du timefuel
        player1.set_fuel(quantitefuel)
    if quantitefuel <= 0:
        launched = False
    rect = pygame.Rect(740, 690, quantitefuel*2, 25)
    pygame.draw.rect(screen, (255, 0, 0), rect)
    text = pygame.font.Font('freesansbold.ttf', 20)
    fuel = text.render('Carburant : {}'.format(player1.get_fuel()), True, (0, 0, 0))
    screen.blit(fuel, (750, 693))

    # Message alerte fuel
    if player1.get_fuel() <= 30:
        text = pygame.font.Font('freesansbold.ttf', 15)
        carb = text.render('Alerte ! Alerte ! Niveau carburant bas', True, (255, 0, 0))
        screen.blit(carb, (400, 200))

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
        plateforme.set_position(0, fallspeed)

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
                    fallspeed = 4
                    game1.add_score(40)
                powerups.remove(objet)
            # print("L'astronaut est sur la ligne de l'objet")


    if (timefuel % 800) == 0:  # On remet la vitesse normal apres le power up
        fallspeed = 0.5

    # Rafraichissement
    pygame.display.flip()

    # à supprimer juste pour get la position du pointeur
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
        print(pygame.mouse.get_pos())  # getposition
