from Model.player import Player
import pygame
from pygame.locals import *

player1 = Player(1, 0, 0, 100)

player_position = (player1.get_x(), player1.get_y())

print("La position courante du joueur est ", player_position)

player1.set_x(int(768/2))
player1.set_y(int(1024/2))
player_position = (player1.get_x(), player1.get_y())

print("La position courante du joueur est ", player_position)

#Test des evenements
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                player_position = player1.setPositCourante(x, y)position_perso.move(0, 10)
            if event.key == K_UP:
                player_position = position_perso.move(0, -10)
            if event.key == K_LEFT:
                player_position = position_perso.move(-10, 0)
            if event.key == K_RIGHT:
                player_position = position_perso.move(10, 0)


