import pygame


class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting positions."""
        self.screen = screen

        # * Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')  # Surface object
        # rect of the ship
        self.rect = self.image.get_rect()
        # rect of the screen it should be drawn on
        self.screen_rect = screen.get_rect()

        # * Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        # bottom of the ship is aligned with the bottom of the screen
        self.rect.bottom = self.screen_rect.bottom

        # * Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
