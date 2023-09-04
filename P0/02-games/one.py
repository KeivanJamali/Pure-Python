import pygame, sys
from pygame import locals as GAME_GLOBALS
from pygame import event as GAME_EVENTS

pygame.init()


wn = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Keip S")
wn.fill((255,255,255))

while True:
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == GAME_GLOBALS.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()

    pygame.display.update()