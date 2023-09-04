import pygame, sys, random

pygame.init()
# Load Images for game
icon = pygame.image.load("spaceship.png")
playerimg = pygame.image.load("spaceship2.png")
enemyimg = pygame.image.load("character.png")
background = pygame.image.load("Light Into The Cavern Free Vector.jpg")
bulletimg = pygame.image.load("bullet.png")

###--------------------------------------------------------------------

# creat window screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_icon(icon)

###--------------------------------------------------------------------

### properties
# player
player_x = 370
player_y = 510
x_move_l, x_move_r, y_move_u, y_move_d = 0, 0, 0, 0
# enemy
enemy_x = 370
enemy_y = 50
enemy_y_move = random.choice([0.7, -0.7])
bound = False
enemy_up_most = 0
enemy_down_most = 50
enemy_speed = -0.7
# bullet
bullet_x = 386
bullet_y = 510
bullet_y_move = random.choice([0.7, -0.7])
bullet_up_most = 0


###--------------------------------------------------------------------

def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def bullet(x, y):
    screen.blit(bulletimg, (x, y))


while True:
    # screen color1
    screen.fill((100, 0, 150))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        # keyboard(keydown and ups)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_move_l = -1
            if event.key == pygame.K_RIGHT and player_x < 800:
                x_move_r = 1
            if event.key == pygame.K_UP and player_y > 0:
                y_move_u = -0.7
            if event.key == pygame.K_DOWN and player_y < 600:
                y_move_d = 0.7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_move_l = 0
            if event.key == pygame.K_RIGHT:
                x_move_r = 0
            if event.key == pygame.K_UP:
                y_move_u = 0
            if event.key == pygame.K_DOWN:
                y_move_d = 0

        # quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()







    bullet(bullet_x, bullet_y)

    player_x += x_move_l + x_move_r
    if player_x <= 0:
        player_x = 0
    elif player_x >= 737:
        player_x = 737
    player_y += y_move_u + y_move_d
    if player_y <= 450:
        player_y = 450
    elif player_y >= 537:
        player_y = 537
    player(player_x, player_y)

    enemy_x += enemy_speed
    enemy_y += enemy_y_move
    if enemy_x <= 0:
        enemy_speed *= -1
        enemy_x += 50
        enemy_y += 50
        enemy_up_most += 50
        enemy_down_most += 50
    if enemy_x >= 737:
        enemy_speed *= -1

    if enemy_down_most >= 500:
        print("Game Over")

    if enemy_y <= enemy_up_most or enemy_y >= enemy_down_most:
        enemy_y_move *= -1

    enemy(enemy_x, enemy_y)

    pygame.display.update()
