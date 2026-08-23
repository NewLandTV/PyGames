"""
Graphics Test
Creation Date: 2023.05.27. Sat, 22:18:00
Modified Date: 2023.05.27. Sat, 22:34:54
"""
# Imports
import pygame

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Show Test")

# Clock
clock = pygame.time.Clock()

# Flags
running = True

# Variables
userInput = ""

while running:
    # Process event
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                userInput = ""
            elif event.key == pygame.K_BACKSPACE:
                userInput = userInput[:-1]
            else:
                userInput += event.unicode
        elif event.type == pygame.QUIT:
            running = False

            pygame.quit()

    # Input
    font = pygame.font.SysFont("arial", 40, True, False)
    text = font.render(userInput, True, BLACK)
    textRect = text.get_rect()
    textRect.centerx = round(SCREEN_WIDTH >> 1)
    textRect.y = 30

    screen.fill(WHITE)
    screen.blit(text, textRect)

    pygame.display.flip()

    clock.tick(60)