import pygame
from pygame.sprite import Group
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
    ship = Ship(ai_settings, screen)
    # * Make a group for treating more a group of object in the same way
    bullets = Group()

    # * Start the main loop for the game.
    while True:
        # * Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        # * Updates the ship position using the movement flags
        ship.update()
        bullets.update()

        # * Draw the screen
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
