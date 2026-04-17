import pygame

pygame.init() # initializes all the pygame sub-modules

WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

COLOR_RED = (255, 0, 0) # Color red in RGB
# 255 - value for red
# 0 - value for green
# 0 - value for blue
# each color component has a value between 0 and 255
# that is, 8 bits
COLOR_BLUE = (0, 0, 255)

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

# Bigger steps help, but movement is still choppy -
# holding the key doesn't keep moving the circle
# We need a different approach (see 08.py, 09.py and 10.py)
movement_speed = 20

running = True
is_red = True
while running: # game loop
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red # flipping the value
                # True -> False and vice versa
            if event.key == pygame.K_UP:
                circle_y -= movement_speed
            if event.key == pygame.K_DOWN:
                circle_y += movement_speed
            if event.key == pygame.K_RIGHT:
                circle_x += movement_speed
            if event.key == pygame.K_LEFT:
                circle_x -= movement_speed
    
    # fill the screen with a color to wipe away anything from last frame
    if is_red:
        screen.fill(COLOR_RED)
        pygame.draw.circle(screen, COLOR_BLUE, (circle_x, circle_y), 40)
    else:
        screen.fill(COLOR_BLUE)
        pygame.draw.circle(screen, COLOR_RED, (circle_x, circle_y), 40)
    
    pygame.display.flip() # updates the screen