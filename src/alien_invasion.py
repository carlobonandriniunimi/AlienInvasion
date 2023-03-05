import sys

import pygame
from settings import Settings


def run_game():
    # * Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    # Returns a surface (display) object of specified size.
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # Sets window name
    pygame.display.set_caption("Alien Invasion")

    # * Start the main loop for the game.
    while True:
        # * Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)

        # * Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
