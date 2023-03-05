import pygame


class Ship():

    def __init__(self, ai_setting, screen):
        """Initialize the ship and set its starting positions."""
        self.screen = screen
        self.ai_settings = ai_setting

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

        # * Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # * Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # * Updates the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Updates the rect object from self.center (only stores integer portion)
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
