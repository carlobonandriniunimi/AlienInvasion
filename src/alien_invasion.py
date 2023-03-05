import pygame
from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
    # * Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    # Returns a surface (display) object of specified size.
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # Sets window name
    pygame.display.set_caption("Alien Invasion")

    # * Make a ship.
    ship = Ship(screen)

    # * Start the main loop for the game.
    while True:
        # * Watch for keyboard and mouse events.
        gf.check_events(ship)

        # * Updates the ship position using the movement flags
        ship.update()

        # * Draw the screen
        gf.update_screen(ai_settings, screen, ship)


run_game()
