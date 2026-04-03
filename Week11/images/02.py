# pygame.transform.rotate() - rotating an image around its center

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

image = pygame.image.load("car.png")
angle = 0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle += 3
    if keys[pygame.K_RIGHT]:
        angle -= 3

    # rotate() creates a NEW surface - it doesn't modify the original
    # Always rotate the original image, not the already-rotated one,
    # to avoid quality loss from repeated rotations
    image = pygame.transform.rotate(image, angle)

    # After rotation the image size changes, so we recalculate
    # the position to keep it centered on screen
    rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill("white")
    screen.blit(image, rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()