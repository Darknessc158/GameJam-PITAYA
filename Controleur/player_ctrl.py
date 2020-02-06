#Import
import sys
sys.path.append('../GameJam-PITAYA/View')
sys.path.append('../GameJam-PITAYA/Model')

import pygame
from Model.player import  Player
from Model.game import Game
from pygame.locals import *
import time as T

def launch() :

    # Creation d'un joueur au centre de la map
    player1 = Player(1, int(1024/2)-40, int(768/2)-40, 100)
    player_position = (player1.get_x(), player1.get_y())
    quantitefuel = player1.get_fuel()

    #Creation d'une game
    game1 = Game(0, 0)# score et time
    #Creation plateforme
    plateformes = game1.generatePlateformes().copy()
    #Creation objet
    powerups = game1.generate_objet().copy()

    # Test des evenements
    pygame.init()
    screen = pygame.display.set_mode((1024, 768), RESIZABLE)


    # Background
    fond = pygame.image.load("../Model/data/map_background.png").convert() #map jusqu'a 10000px
    defilmap = -14000
    # Chargement et collage du personnage
    # convert alpha pour la transparance du png
    perso = pygame.image.load("../Model/data/cosmonaut-idle-100.png") #image du perso de base
    background_objects = [[0.25, [120, 10, 70, 400]], [0.25, [280, 30, 40, 400]], [0.5, [30, 40, 40, 400]],
                          [0.5, [130, 90, 100, 400]], [0.5, [300, 80, 120, 400]]]
    ## ici variables pour retenir en mémoire l’état des touches

    #variable deplacement
    droite = False
    gauche = False
    haut = False
    bas = False
    fall = True
    boost = False
    fuelHit = False
    niveauFall = 0
    fallspeed = 1

    listekeypressed = []

    fall = True # de base le perso chute

    #timeinsecond = int(time.time() % 60)

    timefuel = 0
    nbboucle = 0
    boucle = 0
    true_scroll = [0, 0]
    launched = True
    powerup = False #powerup actif ou non
    propulsion = pygame.image.load("../Model/data/air_propulsion.png")
    estSurPlateforme = False
    new_game = True

    def crash():
        crash= True
        text = pygame.font.Font('freesansbold.ttf', 50)
        fuel = text.render("Crash", True, (0, 0, 0))
        screen.blit(fuel, (500, 400))

        while crash:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.KEYDOWN:
                    crash = False
        pygame.display.flip()
    while launched:
        if (new_game):
            time_var = T.time()
            new_game = False
        fall = True  # Pour le faire rechuter quand il quitte la plateforme
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False
            elif event.type == pygame.KEYDOWN: #Si une touche est enfoncée
                listekeypressed.append(event.key) #insertion des touches enfoncées dans la liste
                if pygame.K_RIGHT in listekeypressed:
                    perso = pygame.image.load("../Model/data/cosmonaut-idle2-100.png")
                    #Sprite droit
                    droite = True
                    if estSurPlateforme == True:
                        perso = pygame.image.load("../Model/data/cosmonaut-march-100.png")
                elif pygame.K_LEFT in listekeypressed:
                    perso = pygame.image.load("../Model/data/cosmonaut-idle-100-gauche.png")
                    gauche = True
                    if estSurPlateforme == True:
                        perso = pygame.image.load("../Model/data/cosmonaut-march-100-gauche.png")
                if pygame.K_UP in listekeypressed:
                    perso = pygame.image.load("../Model/data/cosmonaut-jump-wind-100-gauche.png")
                    haut = True
                    if estSurPlateforme == False:
                        fall = True
                        if pygame.K_LEFT in listekeypressed:
                            perso = pygame.image.load("../Model/data/cosmonaut-idle-100-gauche.png")
                        elif pygame.K_RIGHT in listekeypressed:
                            perso = pygame.image.load("../Model/data/cosmonaut-idle2-100.png")
                        else:
                            perso = pygame.image.load("../Model/data/cosmonaut-jump-100.png")

                elif pygame.K_DOWN in listekeypressed:
                    perso = pygame.image.load("../Model/data/cosmonaut-jump-100.png")
                    bas = True

            elif event.type == pygame.KEYUP: #Si une touche est relachée
                if len(listekeypressed) != 0:
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
        max_x = int(player1.get_x() + 65)
        min_y = int(player1.get_y())
        max_y = int(player1.get_y() + 90)

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
            file_highscore = open("../Model/highscore.txt", "a")
            file_highscore.write(str(game1.get_score()) + "\n")
            file_highscore.close()
            crash()
            new_game = True


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
                if (min_yplat - 10) <= max_y <= (min_yplat + 10):  # colisation par en haut
                    if plateforme.get_type() == 'poison':
                        launched = False
                        file_highscore = open("../Model/highscore.txt", "a")
                        file_highscore.write(str(game1.get_score()) + "\n")
                        file_highscore.close()
                        new_game = True

                    elif plateforme.get_type() == 'teleportation':
                        player_position = player1.movePositTeleportation()
                    elif plateforme.get_type() == 'CarburantMoins':
                        player1.remove_fuel()
                        fuelHit = True
                    bas = False
                    fall = False
                    player_position = player1.movePositCourante(0, fallspeed)  # descends à la vitesse des plateformes
                    # Rechargement du fuel
                    player1.add_fuel(0.2)
                    quantitefuel = int(player1.get_fuel())

            if min_y <= min_yplat and max_y >= max_yplat and powerup == False:  # Est sur la largeur de la plateforme
                if (max_xplat - 5) <= min_x <= (max_xplat + 5):  # collision par la droite (petite marge pour eviter les bug de traversement)
                    gauche = False
                if (min_xplat - 5) <= max_x <= (min_xplat + 5):  # collision par la gauche
                    droite = False

            if min_y <= min_yplat and max_y >= max_yplat and powerup == False and min_xplat <= max_x and min_x <= max_xplat:# Il est sur une plateforme
                fall = False
                estSurPlateforme = True
            else:
                estSurPlateforme = False

        # Re-collage du fond et du player
        defilmap += 1  # defilement de la map
        screen.blit(fond, (0, defilmap))  # recollage map

        # Re-collage
        defilmap += 1 #defilement de la map
        screen.blit(fond, (0, defilmap))
        if defilmap == 0:
            screen.fill((0, 0, 0))
        screen.blit(perso, player_position)
        if haut == True: #Affichage de la propulsion (rajouter le son de la propulsion ici)
            screen.blit(propulsion, ((min_x -15), max_y))

        
        # Fuel
        timefuel += 1
        if (timefuel % 20) == 0: #Retourne la duree depuis que pygame.init a été appeler en ms
            quantitefuel -= 1 #diminue de 1 le fuel à chaque boucle modulo 20 du timefuel
            player1.set_fuel(quantitefuel)
        if quantitefuel <= 0:
            launched = False
            file_highscore = open("../Model/highscore.txt", "a")
            file_highscore.write(str(game1.get_score()) + "\n")
            file_highscore.close()
            new_game = True
        rect = pygame.Rect(740, 677, quantitefuel*2, 25)
        pygame.draw.rect(screen, (255, 0, 0), rect)
        text = pygame.font.Font('freesansbold.ttf', 20)
        fuel = text.render('Carburant : {}'.format(int(player1.get_fuel())), True, (0, 0, 0))
        screen.blit(fuel, (750, 680))

        #Fuel reduit alert
        if fuelHit == True:
            text = pygame.font.Font('freesansbold.ttf', 85)
            carb = text.render('-75', True, (255, 0, 0))
            screen.blit(carb, (900, 650))
            fuelHit = False

        # Message alerte fuel
        if player1.get_fuel() <= 30:
            text = pygame.font.Font('freesansbold.ttf', 25)
            carb = text.render('Alerte ! Alerte ! Niveau carburant bas', True, (255, 0, 0))
            screen.blit(carb, (325, 200))


        # Score
        game1.set_time(int(pygame.time.get_ticks()/1000)) #time in ms depuis pygame.init()
        if (timefuel % 50) == 0:# ajout de score vitesse de base
            game1.add_score(1)
        text = pygame.font.Font('freesansbold.ttf', 50)
        text2 = pygame.font.Font('freesansbold.ttf', 15)
        score = text.render('Score : {}'.format(game1.get_score()), True, (0, 0, 0))
        time_end= T.time()
        time = text2.render('Temps : {} secondes'.format(int(time_end-time_var)), True, (0, 0, 0))
        screen.blit(score, (20, 20))
        screen.blit(time, (20, 60))


        # Collage des plateformes sur l'ecran
        timesprite = 1000;
        for plateforme in plateformes:
            if plateforme.get_y() >= 0 and plateforme.get_y() <= 768:
                if(plateforme.get_type() == 'poison'):
                    if plateforme.get_long() == 50:
                        if (boucle % timesprite) == 0:
                            pique = pygame.image.load("../Model/data/plateformes/pike_50_1.png")
                        else:
                            pique = pygame.image.load("../Model/data/plateformes/pike_50_2.png")
                    elif plateforme.get_long() == 100:
                        if (boucle % timesprite) == 0:
                            pique = pygame.image.load("../Model/data/plateformes/pike_100_1.png")
                        else:
                            pique = pygame.image.load("../Model/data/plateformes/pike_100_2.png")
                    elif plateforme.get_long() == 150:
                        if (boucle % timesprite) == 0:
                            pique = pygame.image.load("../Model/data/plateformes/pike_150_1.png")
                        else:
                            pique = pygame.image.load("../Model/data/plateformes/pike_150_2.png")
                    screen.blit(pique, (plateforme.get_x(), plateforme.get_y()))
                elif(plateforme.get_type() == 'teleportation'):
                    if plateforme.get_long() == 50:
                        if (boucle % timesprite) == 0:
                            portal = pygame.image.load("../Model/data/plateformes/portal_50_1.png")
                        else:
                            portal = pygame.image.load("../Model/data/plateformes/portal_50_2.png")
                    elif plateforme.get_long() == 100:
                        if (boucle % timesprite) == 0:
                            portal = pygame.image.load("../Model/data/plateformes/portal_100_1.png")
                        else:
                            portal = pygame.image.load("../Model/data/plateformes/portal_100_2.png")
                    elif plateforme.get_long() == 150:
                        if (boucle % timesprite) == 0:
                            portal = pygame.image.load("../Model/data/plateformes/portal_150_1.png")
                        else:
                            portal = pygame.image.load("../Model/data/plateformes/portal_150_3.png")

                    screen.blit(portal, (plateforme.get_x(), plateforme.get_y()))
                elif(plateforme.get_type() == 'CarburantMoins'):
                    if plateforme.get_long() == 50:
                        if (boucle % timesprite) == 0:
                            fire = pygame.image.load("../Model/data/plateformes/fire_50_1.png")
                        else:
                            fire = pygame.image.load("../Model/data/plateformes/fire_50_2.png")
                    elif plateforme.get_long() == 100:
                        if (boucle % timesprite) == 0:
                            fire = pygame.image.load("../Model/data/plateformes/fire_100_1.png")
                        else:
                            fire = pygame.image.load("../Model/data/plateformes/fire_100_2.png")
                    elif plateforme.get_long() == 150:
                        if (boucle % timesprite) == 0:
                            fire = pygame.image.load("../Model/data/plateformes/fire_150_1.png")
                        else:
                            fire = pygame.image.load("../Model/data/plateformes/fire_150_2.png")
                    screen.blit(fire, (plateforme.get_x(), plateforme.get_y()))
                else:
                    if plateforme.get_long() == 50:
                        cloud = pygame.image.load("../Model/data/plateformes/cloud_50.png")
                    elif plateforme.get_long() == 100:
                        cloud = pygame.image.load("../Model/data/plateformes/cloud_100.png")
                    elif plateforme.get_long() == 150:
                        cloud = pygame.image.load("../Model/data/plateformes/cloud_150.png")
                    screen.blit(cloud, (plateforme.get_x(), plateforme.get_y()))
            #Chute des plateformes
            if plateforme.get_y() <= 800:
                plateforme.set_position(0, fallspeed)
        # screen.blit(perso, player_position)

        #Augmentation de difficulte
        if timefuel % 500 == 0:
            niveauFall += 1
            fallspeed += 0.25
            print(niveauFall)
        #Power up
        for objet in powerups:
            if objet.get_y() >= 0 and objet.get_y() <= 768:
                if (objet.get_name() == "carburant"):
                    # pygame.draw.circle(screen, (255, 0, 0), (objet.get_x(), objet.get_y()), 40, False)
                    fuelimg = pygame.image.load("../Model/data/fuel.png")
                    screen.blit(fuelimg, (objet.get_x(), objet.get_y()))
                elif (objet.get_name() == "bouteille"):
                    # pygame.draw.circle(screen, (128, 128, 128), (objet.get_x(), objet.get_y()), 20)
                    bottleimg = pygame.image.load("../Model/data/oxygen_tank.png")
                    screen.blit(bottleimg, (objet.get_x(), objet.get_y()))

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
                            fallspeed = fallspeed + 4
                            fall = False
                            powerup = True
                            game1.add_score(40)
                            nbboucle = boucle
                        powerups.remove(objet)
            #Desactivation de l'effet du powerup
            if nbboucle <= (boucle-150) and powerup == True:  # On remet la vitesse normal apres 200 boucles
                fallspeed = fallspeed - 4
                fall = True
                powerup = False
            #chute des objets
            if objet.get_y() <= 800:
                objet.set_position(0, fallspeed)

        ## Traitement des deplacements
        # Droite / Gauche
        if droite:
                player_position = player1.movePositCourante(3.75, 0)
                player_position = player1.movePositCourante(0, 0.25)# chute
        elif gauche:
                player_position = player1.movePositCourante(-3.75, 0)
                player_position = player1.movePositCourante(0, 0.25)# chute
        # Haut / Bas
        if haut:
            if niveauFall == 0 or niveauFall == 1:
                player_position = player1.movePositCourante(0, -0.50)
                player_position = player1.movePositCourante(0, -1.5)
                player_position = player1.movePositCourante(0, -3.5)
            elif niveauFall == 2 or niveauFall == 3 :
                player_position = player1.movePositCourante(0, -1.5)
                player_position = player1.movePositCourante(0, -2.5)
                player_position = player1.movePositCourante(0, -4.25)
            else:
                player_position = player1.movePositCourante(0, -2.25)
                player_position = player1.movePositCourante(0, -2.75)
                player_position = player1.movePositCourante(0, -4.75)

        elif bas:
                player_position = player1.movePositCourante(0, 5)
        # Chute
        if fall:
            if niveauFall == 0:
                player_position = player1.movePositCourante(0, 2.5)
            elif niveauFall == 1:
                player_position = player1.movePositCourante(0, 2.75)
            elif niveauFall == 2:
                player_position = player1.movePositCourante(0, 3)
            elif niveauFall == 3:
                player_position = player1.movePositCourante(0, 3.25)
            elif niveauFall == 4:
                player_position = player1.movePositCourante(0, 3.50)
            elif niveauFall == 5:
                player_position = player1.movePositCourante(0, 3.75)
            elif niveauFall == 6:
                player_position = player1.movePositCourante(0, 4)
            elif niveauFall == 7:
                player_position = player1.movePositCourante(0, 4.25)
            elif niveauFall == 8:
                player_position = player1.movePositCourante(0, 5.50)
            elif niveauFall > 8:
                player_position = player1.movePositCourante(0, 6)


        # recollage du pers
        screen.blit(perso, player_position)

        # Rafraichissement
        pygame.display.flip()

        boucle += 1

