import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0]  == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

cobra = [(200, 200), (210, 200), (220, 200)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.type == K_UP:
                my_direction = UP
            if event.type == K_DOWN:
                my_direction = DOWN
            if event.type == K_RIGHT:
                my_direction = RIGHT
            if event.type == K_LEFT:
                my_direction = LEFT

    if collision(cobra[0], apple_pos):
        apple_pos = on_grid_random()
        cobra.append((0,0))

    for i in range(len(cobra)  -1,  0 , -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if my_direction == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if my_direction == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if my_direction == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if my_direction == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in cobra:
        screen.blit(cobra_skin,pos)

    pygame.display.update()