import pygame
from pygame.locals import *

# Main Menu
def regles_menu():
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
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                menu = False

        title = text_format("REGLES", font, 50, white)
        title_rect = title.get_rect()

        #text_regles = text_format("1969, les Americains ont atteri sur la Lune. \n Ta mission : atterir sur Mars. Bonne chance. Космическая программа !", font, 35, (153,153,0))
        #regles_rect=text_regles.get_rect()

        nuage = pygame.image.load("../Model/data/plateformes/cloud_150.png").convert_alpha()
        nuages_regles = text_format("  : Plateforme solide, recharge lentement la bouteille aussi", font, 25, (153,153,0))
        nuage_rect = nuages_regles.get_rect()

        poison = pygame.image.load("../Model/data/plateformes/pike_150_1.png").convert_alpha()
        poison_regles = text_format(" : Plateforme radioactive, mort instantanee ", font, 25, (153,153,0))
        poison_rect = poison_regles.get_rect()

        teleportation = pygame.image.load("../Model/data/plateformes/portal_150_1.png").convert_alpha()
        teleportation_regles = text_format(" : Plateforme trou noir, permet une teleportation    ", font, 25, (153,153,0))
        teleportation_rect = teleportation_regles.get_rect()

        feu = pygame.image.load("../Model/data/plateformes/fire_150_1.png").convert_alpha()
        feu_regles = text_format(" : Plateforme feu, en contact carburant reduit à 25% ", font, 25, (153,153,0))
        feu_rect = feu_regles.get_rect()

        booster = pygame.image.load("../Model/data/oxygen_tank.png").convert_alpha()
        booster_regles = text_format(" : Power-up booster permet une acceleration verticale  ", font, 25, (153,153,0))
        booster_rect = booster_regles.get_rect()

        canister = pygame.image.load("../Model/data/fuel.png").convert_alpha()
        canister_regles = text_format(" : Recharge bouteille permet de remplir votre reservoir air ", font, 25, (153,153,0))
        canister_rect = canister_regles.get_rect()

        # Main Menu UI
        screen.fill(black)
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 50))
        screen.blit(nuage, (15,175))
        screen.blit(nuages_regles, (200,165))
        screen.blit(poison, (15, 275))
        screen.blit(poison_regles, (200, 265))
        screen.blit(teleportation, (15, 370))
        screen.blit(teleportation_regles, (200, 360))
        screen.blit(feu, (15, 470))
        screen.blit(feu_regles, (200, 460))
        screen.blit(booster, (80, 545))
        screen.blit(booster_regles, (200, 570))
        screen.blit(canister, (70, 645))
        screen.blit(canister_regles, (200, 657))



        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Gorgobalt in the Sky")




