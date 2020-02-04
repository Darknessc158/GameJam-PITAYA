import sys

import pygame
from pygame.locals import *
sys.path.append('/home/soysauceduck/IUT/GameJam/GameJam-PITAYA/Controleur')
sys.path.append('/home/soysauceduck/IUT/GameJam/GameJam-PITAYA/Model')
from menu import Menu

# Setup pygame/window ---------------------------------------- #
class VueMenu:
    mainClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('game base')
    screen = pygame.display.set_mode((1024, 768), 0, 32)
    font = pygame.font.SysFont( None, 20)


    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        
    menu1 = Menu()
    menu1.main_menu(screen, font, mainClock)
