import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 768))

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
