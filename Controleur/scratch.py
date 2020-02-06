
import pygame
import main
import player_ctrl
import  options
from pygame.locals import *

# Game Initialization

pygame.init()
file = '../Model/data/Digital Native.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
# Music

# Game Resolution
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))

#Background image
background = pygame.image.load("../Model/data/background.png").convert()
background_rect = background.get_rect()
title = pygame.image.load("../Model/data/Gorgobalt-In-The-Sky.png").convert_alpha()
title_rect = title.get_rect()

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = 'freesansbold.ttf'

# Game Framerate
clock = pygame.time.Clock()
FPS = 30



# Main Menu
def main_menu():
    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and selected == "start":
                    selected = "start"
                elif event.key == pygame.K_DOWN and selected == "start":
                    selected = "highscore"
                elif event.key == pygame.K_UP and selected == "highscore":
                    selected = "start"
                elif event.key == pygame.K_DOWN and selected == "highscore":
                    selected = "options"
                elif event.key == pygame.K_UP and selected == "options":
                    selected = "highscore"
                elif event.key == pygame.K_DOWN and selected == "options":
                    selected = "quit"
                elif event.key == pygame.K_UP and selected == "quit":
                    selected = "options"
                elif event.key == pygame.K_DOWN and selected == "quit":
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        player_ctrl.launch()
                    if  selected == "highscore":
                        main.highscore_menu()
                    if  selected == "options":
                        options.options_menu()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.blit(background, background_rect)
        if selected == "start":
            text_start = text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, (153,153,0))
        if selected == "options":
            text_options = text_format("OPTIONS", font, 75, white)
        else:
            text_options = text_format("OPTIONS", font, 75, (153,153,0))
        if selected == "highscore":
            text_highscore = text_format("HIGHSCORE", font, 75, white)
        else:
            text_highscore = text_format("HIGHSCORE", font, 75, (153,153,0))
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, (80,80,80))
        else:
            text_quit = text_format("QUIT", font, 75, (153,153,0))

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        highscore_rect=text_highscore.get_rect()
        options_rect= text_options.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 10))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 150))
        screen.blit(text_highscore, (screen_width / 2 - (highscore_rect[2] / 2), 300))
        screen.blit(text_options, (screen_width / 2 - (options_rect[2] / 2), 450))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 600))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Gorgobalt in the Sky")



 # Initialize the Game
main_menu()
pygame.quit()
quit()