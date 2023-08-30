import pygame
import random

# Global variables
SCREENWIDTH = 289
SCREENHEIGHT = 511
FPS = 32

# Load the images
background = pygame.image.load("background.png")
bird = pygame.image.load("bird.png")
pipe1 = pygame.image.load("pipe1.png")
pipe2 = pygame.image.load("pipe2.png")

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game
    bird_y += 0.5
    if bird_y > SCREENHEIGHT - bird.get_height():
        bird_y = 0

    # Draw the game
    screen.blit(background, (0, 0))
    screen.blit(bird, (bird_x, bird_y))

    # Check for collisions
    if bird_y + bird.get_height() >= pipe1_y - pipe1.get_height() and bird_x + bird.get_width() > pipe1_x and bird_x < pipe1_x + pipe1.get_width():
        running = False
    elif bird_y + bird.get_height() >= pipe2_y - pipe2.get_height() and bird_x + bird.get_width() > pipe2_x and bird_x < pipe2_x + pipe2.get_width():
        running = False

    # Flip the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit the game
pygame.quit()
