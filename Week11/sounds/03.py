# pygame.mixer.music - for streaming longer audio tracks (background music)
# Unlike pygame.mixer.Sound (for short effects), music streams from disk
# and only one music track can play at a time

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 200))

# Load a music file (MP3, OGG, WAV)
pygame.mixer.music.load("bonk.mp3")

# Play the music (-1 means loop forever, 0 means play once)
pygame.mixer.music.play(-1)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            if event.key == pygame.K_r:
                pygame.mixer.music.play(-1)

    screen.fill("black")
    font = pygame.font.SysFont("Verdana", 20)
    screen.blit(font.render("P = pause/unpause, S = stop, R = restart", True, "white"), (10, 80))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()