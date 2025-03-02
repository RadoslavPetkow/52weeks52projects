import pygame
import os

MARIO_IMG = pygame.image.load(os.path.join("assets", "sprites", "mario.png"))
MARIO_IMG = pygame.transform.scale(MARIO_IMG, (40, 50))  # Resize if needed

class Player:
    def __init__(self, x, y):
        self.image = MARIO_IMG
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.facing_right = True

    def move(self, keys):
        self.vel_x = 0
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
            self.facing_right = False
        if keys[pygame.K_RIGHT]:
            self.vel_x = 5
            self.facing_right = True
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -15
            self.on_ground = False

    def apply_gravity(self, platforms):
        self.vel_y += 0.6
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform) and self.vel_y >= 0:
                self.rect.bottom = platform.top
                self.vel_y = 0
                self.on_ground = True
        if self.rect.bottom >= 540:
            self.rect.bottom = 540
            self.vel_y = 0
            self.on_ground = True

    def update(self, platforms):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.apply_gravity(platforms)

    def draw(self, screen, camera_x):
        if self.facing_right:
            screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))
        else:
            flipped_image = pygame.transform.flip(self.image, True, False)
            screen.blit(flipped_image, (self.rect.x - camera_x, self.rect.y))