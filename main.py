import pygame
import sys
import random  # Import the random module

# Initialize pygame
pygame.init()

# Game window dimensions for fullscreen
screen_info = pygame.display.Info()  # Get the display size
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Fullscreen mode
pygame.display.set_caption('RPG game')
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
random_color = (255, 0, 0)  # Color for the random rectangles
black = (0, 0, 0)

# Player properties
player_width = 100
player_height = 100
player_x = 0
player_y = 0
player_speed = 5  # Define a speed for smooth movement

# Random rectangle properties
num_rectangles = 10  # Number of random rectangles to generate
rectangles = []  # List to store random rectangles

# Time tracking
delay_time = 3000  # Delay in milliseconds (5 seconds)
function_called = False  # To track if the function has been called
start_time = pygame.time.get_ticks()  # Get the current time

# Function to generate random rectangles
def generate_random_rectangles():
    for _ in range(num_rectangles):
        rect_width = random.randint(50, 150)  # Random width between 50 and 150 pixels
        rect_height = random.randint(50, 150)  # Random height between 50 and 150 pixels
        rect_x = random.randint(0, screen_width - rect_width)  # Random x position
        rect_y = random.randint(0, screen_height - rect_height)  # Random y position
        rectangles.append(pygame.Rect(rect_x, rect_y, rect_width, rect_height))


def rect_movement():
    for rect in rectangles:
        rect[0] -= 10

def draw_rect():
    # Draw the random rectangles
    for rect in rectangles:
        pygame.draw.rect(screen, random_color, rect)

# Generate the initial set of random rectangles
generate_random_rectangles()

paused = False
font = pygame.font.Font(None, 74)  # Font for paused text
paused_text = font.render("Paused", True, white)
paused_text_rect = paused_text.get_rect(center=(screen_width // 2, screen_height // 2))
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused

    if not paused:
        # Clear the screen
        screen.fill(white)

        # Movement logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < screen_height - player_height:
            player_y += player_speed

        current_time = pygame.time.get_ticks()
        if not function_called and current_time - start_time >= delay_time:
            generate_random_rectangles()
            function_called = True  # Ensure the function is called only once

        draw_rect()
        rect_movement()

        # Draw the player
        player_sprite = pygame.draw.rect(screen, blue, [player_x, player_y, player_width, player_height])

    else:
        #what appear if paused
        screen.fill((black))
        screen.blit(paused_text, paused_text_rect)


    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
