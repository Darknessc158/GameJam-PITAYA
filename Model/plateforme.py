import sys
from pygame.locals import *
import pygame


class Plateforme:
    
    def collision_test(self, rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list
