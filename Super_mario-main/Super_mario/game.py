import pygame
from player import Player
from levels.level1 import Level1
from levels.level2 import Level2

def game_loop(level):
    clock = pygame.time.Clock()
    FPS = 120
    player = Player(100, 540)
    running = True
    camera_x = 0

    while running:
        screen = pygame.display.set_mode((800, 600))
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return  # Return to menu

        player.move(keys)
        player.update(level.platforms)

        camera_x = max(0, min(player.rect.x - 400, level.width - 800))

        level.draw(screen, camera_x)
        player.draw(screen, camera_x)

        pygame.display.update()
        clock.tick(FPS)