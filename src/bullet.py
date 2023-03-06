import pygame
from pygame.sprite import Sprite
from settings import Settings


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    # * Note the type annotation for the parameters
    def __init__(self, ai_settings: Settings, screen, ship):
        """Create a bullet object at the ship's current positon."""
        # Python 3: super().__init__()
        super(Bullet, self).__init__()  # ! 2.7 Syntax
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        # Requires the top-left coordinate and width-height
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Sore the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Using float y for more precision
        self.y -= self.speed_factor
        # Updating actual position of the rect as integer
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
