import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Keip Server")
window.fill((255, 255, 255))
gameicon = pygame.image.load("keip.jpg")
pygame.display.set_icon(gameicon)

pygame.draw.rect(window, (0, 255, 0), (5, 300, 990, 100), 10)
pygame.draw.circle(window, (0, 0, 255), (500, 350), 30)
pygame.draw.ellipse(window, (255, 0, 0), (397.5, 122.5, 200, 100), 5)
pygame.draw.polygon(window, (50, 50, 50), ((100, 100), (900, 100), (900, 600), (100, 600)), 1)
pygame.draw.line(window, (0, 0, 0), (0, 700), (1000, 0), 10)
pygame.draw.lines(window, (0, 0, 0), True, ((0, 0), (200, 50), (1000, 700)), 10)
pygame.draw.arc(window, (39, 49, 179), (50, 50, 300, 200), 20, 360, 2)  # ???

while True:
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
