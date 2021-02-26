import pygame
import math
from game import Game
import ctypes  # Screen resolution


user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


pygame.init()

# Init clock
clock = pygame.time.Clock()
FPS = 60

# Get screen resolution
WIDTH = math.ceil(min(1000, screensize[1] - 100) * 0.7)
HEIGHT = min(1000, screensize[1] - 100)

# Generate game's window
pygame.display.set_caption("War Thunder")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Import background
background = pygame.image.load('assets/background_v1.png')

# Import button Start
play_button = pygame.image.load('assets/play_button.jpg')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil((screen.get_width()-352)/2)
play_button_rect.y = math.ceil((screen.get_height()-352)/2)

# load game
game = Game((WIDTH, HEIGHT))

running = True

while running:

    # Apply background
    screen.blit(background, (0, 0))

    if game.is_playing:
        # Start instructions
        game.update(screen)
    else:
        # Add play button
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))

    # Refresh screen
    pygame.display.flip()

    for event in pygame.event.get():
        # END condition
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Identify if a key is pressed
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # Detect if Space bar is pressed
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.shoot()
                else:
                    # Launch game
                    game.start()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check collision with play_button
            if play_button_rect.collidepoint(event.pos):
                # Launch game
                game.start()

    # Fix clock speed
    clock.tick(FPS)
