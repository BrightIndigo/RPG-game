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
green = (0, 255, 0)
red = (255, 0, 0)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.clicked = False

    def draw(self, screen):
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        # Check if mouse is over the button
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        # Render button text
        text_surface = self.font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        # Check if the button is clicked
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed[0] and not self.clicked:
                self.clicked = True
                return True
        if not mouse_pressed[0]:
            self.clicked = False
        return False

# Set up font
font = pygame.font.Font(None, 40)

# Create a button instance
button_width = 200
button_height = 80
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2
button = Button(button_x, button_y, button_width, button_height, "Exit game", green, red, font)

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
paused_text_rect = paused_text.get_rect(center=(screen_width // 2, 50))
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
        button.draw(screen)
        if button.is_clicked():
            running = False


    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
