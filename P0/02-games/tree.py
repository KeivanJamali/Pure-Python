import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Keip S")
window.fill("yellow")
pygame.display.set_icon(pygame.image.load("keip.jpg"))


while True:

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
