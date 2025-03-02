import pygame
import os

class Level:
    def __init__(self, player):
        self.width = 2400  # Level width
        self.height = 600  # Level height
        self.background = None
        self.platforms = []
        self.player = player

    def load_background(self, image_path):
        """Load background image for the level."""
        self.background = pygame.image.load(os.path.join("assets", "backgrounds", image_path))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def create_platforms(self, platform_list):
        """Create platforms for the level."""
        self.platforms = [pygame.Rect(x, y, w, h) for (x, y, w, h) in platform_list]

    def draw(self, screen, camera_x):
        """Draw the level background and platforms."""
        screen.blit(self.background, (-camera_x, 0))
        for platform in self.platforms:
            pygame.draw.rect(screen, (150, 75, 0), (platform.x - camera_x, platform.y, platform.width, platform.height))

    def update(self):
        """Update level elements (e.g., moving platforms, enemies in future)."""
        pass  # Placeholder for future logic