import pygame
from game import game_loop
from levels.level1 import Level1
from levels.level2 import Level2
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 50)

def start_menu():
    while True:
        screen.fill((255, 255, 255))
        title_text = font.render("Super Mario", True, (0, 0, 0))
        level1_text = font.render("Press 1 for Level 1", True, (0, 0, 0))
        level2_text = font.render("Press 2 for Level 2", True, (0, 0, 0))
        screen.blit(title_text, (300, 200))
        screen.blit(level1_text, (250, 300))
        screen.blit(level2_text, (250, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop(Level1(Player(100, 540)))
                if event.key == pygame.K_2:
                    game_loop(Level2(Player(100, 540)))

start_menu()