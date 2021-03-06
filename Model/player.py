import sys
import pygame
from pygame.locals import *
import random

class Player:
    
    def __init__(self, health, x, y, fuel):
        self.x = x  # position x
        self.y = y  # position y
        self.health = health  # Vie du joueur 1 ou 0
        self.fuel = fuel  # quantite de fuel du jetpack du joueur
        self.img = '../GameJam-PITAYA/Model/data/player.png'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_health(self):
        return self.health

    def get_fuel(self):
        return self.fuel

    def get_img(self):
        return self.img

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def movePositCourante(self, x, y):
        self.x += x
        self.y += y
        return (int(self.x), int(self.y))

    def movePositTeleportation(self):
        self.x = random.randrange(10, 980, 25)
        self.y -= 175
        return (self.x, self.y)

    def set_health(self, health):
        self.health = health

    def set_fuel(self, fuel):
        self.fuel = fuel

    def add_fuel(self, fuel):
        self.fuel += fuel
        if self.fuel > 100:
            self.fuel = 100

    def remove_fuel(self):
        self.fuel = 25
        if self.fuel < 0:
            self.fuel = 0

    def full_fuel(self): #rechage à 100 le fuel (max)
        self.fuel = 100

    def deplacement(self, direction):

        if event.type == KEYDOWN:
            g = 0
            if k[K_UP]:
                hero.position.y += hero.v_y
                hero.v_y += hero.v_gravitation

                if hero.v_y > 5:
                    hero.v_y = hero.v_saut

            if k[K_RIGHT]:
                hero.position.x += 5
                hero.image = hero.image_right

                if k[K_RIGHT] and k[K_UP]:
                    hero.position.x += hero.v_x
                    hero.position.y += hero.v_y
                    hero.v_y += hero.v_gravitation
                    hero.image = hero.image_right

                    if hero.v_y > 5:
                        hero.v_y = hero.v_saut

            if k[K_LEFT]:
                hero.position.x -= 5
                hero.image = hero.image_left

                if k[K_LEFT] and k[K_UP]:
                    hero.position.x -= hero.v_x
                    hero.position.y += hero.v_y
                    hero.v_y += hero.v_gravitation
                    hero.image = hero.image_left

                    if hero.v_y > 5:
                        hero.v_y = hero.v_saut

            if k[K_DOWN]:
                hero.position.y += 5
                hero.image = hero.image_left

            if k[K_c]:
                hero.position.y -= 5
                hero.image = hero.image_right

        elif event.type == KEYUP:

            if k[K_UP]:
                hero.v_y = hero.v_saut


    def move(self, rect, movement, tiles, map):
        collision_types = {'top': False, 'bottom': False,
                        'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)

        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)

        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types
