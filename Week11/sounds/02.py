# Playing sounds with a caching pattern
#
# Loading a sound file from disk is slow. If we play the same sound often,
# we should load it once and reuse it. This function caches sounds in a dict

import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
clock = pygame.time.Clock()

# Cache: maps file path -> Sound object (so we only load each file once)
_sound_library = dict()

def play_sound(path):
    global _sound_library
    sound = _sound_library.get(path)
    if sound is None:
        # os.sep is the path separator for the current OS ('/' on mac/linux, '\\' on windows)
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # KEYDOWN fires once per key press - prevents the sound from
        # playing repeatedly on every frame while the key is held down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                play_sound("bonk.mp3")

    screen.fill("white")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()