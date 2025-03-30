import pygame
from screeninfo import get_monitors
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()

for el in get_monitors():
    print(str(el[2]))

screen = pygame.display.set_mode([300, 300])

p_x = 0
p_y = 0

running = True
menu = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT and p_x >= 10:
                p_x -= 10
            elif event.key == K_RIGHT and p_x <= 1920:
                p_x += 10
            elif event.key == K_UP and p_y >= 10:
                p_y -= 10
            elif event.key == K_DOWN and p_y <= 1070:
                p_y += 10
            elif event.key == K_ESCAPE and menu == False:
                pass

    screen.fill((255, 255, 255))

    player = pygame.draw.rect(screen, (100, 100, 100), [p_x, p_y, 100, 100])

    pygame.display.flip()

pygame.quit()