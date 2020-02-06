import pygame
from pygame.locals import *
import regles_menu

# Main Menu
def options_menu():
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
    selected = "regles"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and selected == "regles":
                    selected = "regles"
                elif event.key == pygame.K_DOWN and selected == "regles":
                    selected = "difficulte"
                elif event.key == pygame.K_UP and selected == "difficulte":
                    selected = "regles"
                elif event.key == pygame.K_DOWN and selected == "difficulte":
                    selected = "difficulte"

                if event.key == pygame.K_RETURN:
                    if selected == "regles":
                        regles_menu.regles_menu()
                    if selected == "difficulte":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(black)

        if selected == "regles":
            regles = text_format("Regles", font, 70, white)
        else:
            regles = text_format("Regles", font, 70, yellow)
        if selected == "difficulte":
            difficulte = text_format("Difficulte", font, 70, white)
        else:
            difficulte = text_format("Difficulte", font, 70, yellow)

        title = text_format("OPTIONS", font, 70, white)
        title_rect = title.get_rect()
        regles_rect = regles.get_rect()
        difficulte_rect = difficulte.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(regles, (screen_width / 2 - (regles_rect[2] / 2) , 225))
        screen.blit(difficulte, (screen_width / 2 - (difficulte_rect[2] / 2) , 375))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Gorgobalt in the Sky")




