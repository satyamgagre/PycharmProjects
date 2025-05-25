import pygame
from pygame.locals import *
import random
import time

# Initialize pygame
pygame.init()

# Define color constants
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# Set game window dimensions
win_width = 700
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("THE HUNGRY SERPENT")

# Optional delay to show title screen
time.sleep(2)

# Snake and game speed settings
snake_block = 10
snake_speed = 15

# Clock to control FPS
clock = pygame.time.Clock()

# Load custom fonts (make sure .ttf files are in the same folder)
font_style = pygame.font.Font("PressStart2P.ttf", 14)       # Message font
score_font = pygame.font.Font("VT323-Regular.ttf", 24)      # Score font

# Function to display score
def user_score(score):
    value = score_font.render("Score: " + str(score), True, red)
    window.blit(value, (10, 10))

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Function to display a message (like game over)
def message_display(msg):
    text_surface = font_style.render(msg, True, white)
    text_rect = text_surface.get_rect(center=(win_width / 2, win_height / 2))
    window.blit(text_surface, text_rect)

# Main game loop
def game_loop():
    # Game over flags
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = win_width / 2
    y1 = win_height / 2

    # Movement changes
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0

    while not game_over:

        # Handle game over screen
        while game_close:
            window.fill(black)
            message_display("You Lost! Press S to Restart or Q to Quit")
            user_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_s:
                        game_loop()

        # Event handling (movement)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for boundaries
        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        window.fill(black)

        # Draw food
        pygame.draw.rect(window, yellow, [foodx, foody, snake_block, snake_block])

        # Update snake list
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for collision with self
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        user_score(length_of_snake - 1)
        pygame.display.update()

        # Check if food is eaten
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Control game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
