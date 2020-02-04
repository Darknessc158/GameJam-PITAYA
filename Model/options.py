import pygame
from pygame.locals import *
import sys
from graphic import Figure

class Options:
    def options(self, screen, font, mainClock):
        running = True
        text5 = Figure()
        while running:
            screen.fill((0, 0, 0))

            text5.draw_text('options', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)
