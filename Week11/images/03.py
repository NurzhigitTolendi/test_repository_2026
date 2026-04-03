import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

original_image = pygame.image.load("ryan-gosling.png")
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

    rotated_image = pygame.transform.rotate(original_image, angle)
    rect = rotated_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill("white")
    screen.blit(rotated_image, rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()