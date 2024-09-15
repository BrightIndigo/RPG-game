import pygame
import sys

pygame.init()

#okno gry
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('RPG game')
clock = pygame.time.Clock()

white = (255, 0, 255)
blue = (0, 0, 255)

player_width = 100
player_height = 100
player_x = 0
player_y = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    #tu będę renderował grę!
    player_sprite = pygame.draw.rect(screen, (0, 255, 255), [player_x, player_y, player_width, player_height])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()