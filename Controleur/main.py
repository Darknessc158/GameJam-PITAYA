import pygame
from pygame.locals import *

# Main Menu
def highscore_menu():
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

        # Main Menu UI
        screen.fill(black)
        title = text_format("HIGHSCORE", font, 70, white)
        file_highscore = open("../Model/highscore.txt", "r")
        title_rect = title.get_rect()

        sorted_scores = []
        for line in file_highscore :
            sorted_scores.append(int(line))

        sorted_scores.sort(reverse = True)

        scores = []
        b = 1
        for score in sorted_scores:
            text_score = text_format("Score "+ str(b)+  " :    " + str(score), font, 55, (150,150,150))
            scores.append(text_score)
            b += 1
            if b == 6:
              break
        highscore_rect = text_score.get_rect()


        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))

        i = 250
        for score in scores:
            screen.blit(score, (screen_width / 2 - (highscore_rect[2] / 2), i))
            i += 75
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Gorgobalt in the Sky")




