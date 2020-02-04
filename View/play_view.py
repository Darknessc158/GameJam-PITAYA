import sys
sys.path.append('../GameJam-PITAYA/Controleur')
sys.path.append('../GameJam-PITAYA/Model')

print(sys.path)
import pygame
from pygame.locals import *
from Model.player import Player
from Model.plateforme import Plateforme
clock = pygame.time.Clock()

pygame.init()  # initiates pygame

pygame.display.set_caption('Pygame Platformer')

WINDOW_SIZE = (1024, 768)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window

# used as the surface for rendering, which is scaled
display = pygame.Surface((300, 200))

moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0

game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

grass_img = pygame.image.load(
    '../GameJam-PITAYA/Model/data/grass.png')
dirt_img = pygame.image.load(
    '../GameJam-PITAYA/Model/data/dirt.png')

player_img = pygame.image.load(
    '../GameJam-PITAYA/Model/data/cosmaunaut.png').convert()
player_img.set_colorkey((255, 255, 255))

player_rect = pygame.Rect(100, 100,5,13)

joueur = Player(100,0,0,100)


while True:  # game loop
    display.fill((146, 244, 255))  # clear screen by filling it with blue

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img, (x*16, y*16))
            if tile == '2':
                display.blit(grass_img, (x*16, y*16))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16, y*16, 16, 16))
            x += 1
        y += 1

    player_movement = [0, 0]
    if moving_right == True:
        player_movement[0] += 2
    if moving_left == True:
        player_movement[0] -= 2
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 3

    player_rect, collisions = joueur.move(
        player_rect, player_movement, tile_rects, game_map)

    if collisions['bottom'] == True:
        air_timer = 0
        vertical_momentum = 0
    else:
        air_timer += 1

    display.blit(player_img, (player_rect.x, player_rect.y))

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if air_timer < 6:
                    vertical_momentum = -5
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(60)
