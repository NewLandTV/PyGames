import pygame
import sys

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Load Image")

clock = pygame.time.Clock()
image = pygame.image.load("Image.png")
image = pygame.transform.scale(image, (960, 540))

x = 0

while True:
    clock.tick(30)
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 0))

    x = x + 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

pygame.quit()
sys.exit()