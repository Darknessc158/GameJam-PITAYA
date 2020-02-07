
import pygame
from pygame.locals import *

# Game Initialization
def difficulty_menu():
    # Game Initialization
    pygame.init()

    # Game Resolution
    screen_width = 1024
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))

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

    menu = True
    selected = "Facile"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and selected == "Facile":
                    selected = "Retour"
                elif event.key == pygame.K_DOWN and selected == "Facile":
                    selected = "Intermediaire"
                elif event.key == pygame.K_UP and selected == "Intermediaire":
                    selected = "Facile"
                elif event.key == pygame.K_DOWN and selected == "Intermediaire":
                    selected = "Pro"
                elif event.key == pygame.K_UP and selected == "Pro":
                    selected = "Intermediaire"
                elif event.key == pygame.K_DOWN and selected == "Pro":
                    selected = "Impossible"
                elif event.key == pygame.K_UP and selected == "Impossible":
                    selected = "Pro"
                elif event.key == pygame.K_DOWN and selected == "Impossible":
                    selected = "Retour"
                elif event.key == pygame.K_UP and selected == "Retour":
                    selected = "Impossible"
                elif event.key == pygame.K_DOWN and selected == "Retour":
                    selected = "Facile"
                if event.key == pygame.K_RETURN:
                    if selected == "Facile":
                        file_difficulty = open("../Model/difficulty.txt", "w").close()
                        file_difficulty = open("../Model/difficulty.txt", "w")
                        file_difficulty.write("1")
                        file_difficulty.close()
                        menu = False
                    if  selected == "Intermediaire":
                        file_difficulty = open("../Model/difficulty.txt", "w").close()
                        file_difficulty = open("../Model/difficulty.txt", "w")
                        file_difficulty.write("2")
                        file_difficulty.close()
                        menu = False
                    if  selected == "Pro":
                        file_difficulty = open("../Model/difficulty.txt", "w").close()
                        file_difficulty = open("../Model/difficulty.txt", "w")
                        file_difficulty.write("3")
                        file_difficulty.close()
                        menu = False
                    if  selected == "Impossible":
                        file_difficulty = open("../Model/difficulty.txt", "w").close()
                        file_difficulty = open("../Model/difficulty.txt", "w")
                        file_difficulty.write("5")
                        file_difficulty.close()
                        menu = False
                    if selected == "Retour":
                        menu = False


        # Main Menu UI
        screen.fill(black)
        title = text_format("Difficulte", font, 70, white)

        if selected == "Facile":
            text_start = text_format("FACILE", font, 75, white)
        else:
            text_start = text_format("FACILE", font, 75, (153,153,0))
        if selected == "Intermediaire":
            text_options = text_format("AVANCE", font, 75, white)
        else:
            text_options = text_format("AVANCE", font, 75, (153,153,0))
        if selected == "Pro":
            text_highscore = text_format("PRO", font, 75, white)
        else:
            text_highscore = text_format("PRO", font, 75, (153,153,0))
        if selected == "Impossible":
            text_quit = text_format("IMPOSSIBLE", font, 75, (255,0,0))
        else:
            text_quit = text_format("IMPOSSIBLE", font, 75, (153,153,0))
        if selected == "Retour":
            retour = text_format("Retour", font, 60, white)
        else:
            retour = text_format("Retour", font, 60, yellow)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        highscore_rect=text_highscore.get_rect()
        options_rect= text_options.get_rect()
        quit_rect = text_quit.get_rect()
        retour_rect = retour.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 10))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 150))
        screen.blit(text_options, (screen_width / 2 - (options_rect[2] / 2), 250))
        screen.blit(text_highscore, (screen_width / 2 - (highscore_rect[2] / 2), 350))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 450))
        screen.blit(retour, (screen_width / 2 - (retour_rect[2] / 2), 600))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Gorgobalt in the Sky")



