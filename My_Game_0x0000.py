"""
My Game 0x0000
Creation Date: 2022.04.30. Sat, 08:25:26 (A.M.)
Modified Date: 2022.04.30. Sat, 08:44:33 (A.M.)
"""
import pygame

# Pygame initialized
pygame.init()

# Set window width and height
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

# RGB color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Window Setting
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Game (0x0000)")

# Background colot setting
display_surface.fill(BLUE)

# Using the line function it draw a line
pygame.draw.line(display_surface, RED, (0, 300), (WINDOW_WIDTH, 300), 3)

# Using the circle function it draw a circle
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 50, 3)

# Game is running event
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display update
    pygame.display.update()

pygame.quit()
