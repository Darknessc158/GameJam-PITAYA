import pygame
from pygame.locals import *
import sys
from options import Options
from game import Game
from graphic import Figure
class Menu:
    

    mainClock = pygame.time.Clock()
    def main_menu(self, screen, font, mainClock):
        text1 = Figure()
        text2 = Figure()
        text3 = Figure()
        text4 = Figure()
        text5 = Figure()
        play = Game(0,0)
        option = Options()
        click = False
        while True:
            
            screen.fill((0, 0, 0))
            text1.draw_text('Main Menu', font, (255, 255, 255), screen, 20, 20)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(50, 500, 200, 50)
            button_2 = pygame.Rect(50, 600, 200, 50)
            if button_1.collidepoint((mx, my)):
                if click:
                    play.game(mainClock)
            if button_2.collidepoint((mx, my)):
                if click:
                    option.options(screen, font, mainClock)
            pygame.draw.rect(screen, (255, 0, 0), button_1)
            pygame.draw.rect(screen, (255, 0, 0), button_2)
            text2.draw_text('Nom du Jeu', pygame.font.SysFont(
                None, 100), (255, 255, 255), screen, 60, 200)
            text3.draw_text('Play', pygame.font.SysFont(None, 50),
                    (255, 255, 255), screen, 60, 510)
            text4.draw_text('Options', pygame.font.SysFont(
                None, 50), (255, 255, 255), screen, 60, 610)
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            mainClock.tick(60)

    
