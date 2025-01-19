import pygame
import random

pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
BLOCK_SIZE = 30
PLAY_WIDTH = 10
PLAY_HEIGHT = 20

BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GRAY    = (128, 128, 128)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
ORANGE  = (255, 165, 0)
CYAN    = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW  = (255, 255, 0)

S = [
    [(0,0),(1,0),(1,1),(2,1)],
    [(2,0),(1,1),(2,1),(1,2)]
]
Z = [
    [(1,0),(2,0),(0,1),(1,1)],
    [(1,0),(1,1),(2,1),(2,2)]
]
I = [
    [(0,0),(1,0),(2,0),(3,0)],
    [(2,0),(2,1),(2,2),(2,3)]
]
O = [
    [(0,0),(1,0),(0,1),(1,1)]
]
J = [
    [(0,0),(0,1),(1,1),(2,1)],
    [(1,0),(2,0),(1,1),(1,2)],
    [(0,1),(1,1),(2,1),(2,0)],
    [(1,0),(1,1),(1,2),(0,2)]
]
L = [
    [(2,0),(0,1),(1,1),(2,1)],
    [(1,0),(1,1),(1,2),(2,2)],
    [(0,1),(1,1),(2,1),(0,2)],
    [(1,0),(1,1),(1,2),(0,0)]
]
T = [
    [(1,0),(0,1),(1,1),(2,1)],
    [(1,0),(1,1),(2,1),(1,2)],
    [(0,1),(1,1),(2,1),(1,2)],
    [(1,0),(0,1),(1,1),(1,2)]
]

SHAPES = [S, Z, I, O, J, L, T]
SHAPE_COLORS = [GREEN, RED, CYAN, YELLOW, BLUE, ORANGE, MAGENTA]

class Piece:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.rotation = 0
    def image(self):
        return self.shape[self.rotation]
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

def create_grid(locked_positions):
    grid = [[BLACK for _ in range(PLAY_WIDTH)] for _ in range(PLAY_HEIGHT)]
    for (x, y), color in locked_positions.items():
        grid[y][x] = color
    return grid

def valid_space(piece, grid):
    spots = [[(j,i) for j in range(PLAY_WIDTH) if grid[i][j] == BLACK] for i in range(PLAY_HEIGHT)]
    spots = [p for row in spots for p in row]
    for (x, y) in piece.image():
        if (piece.x + x, piece.y + y) not in spots:
            if piece.y + y > -1:
                return False
    return True

def check_lost(positions):
    for (_, y) in positions:
        if y < 1:
            return True
    return False

def get_shape():
    shape = random.choice(SHAPES)
    color = SHAPE_COLORS[SHAPES.index(shape)]
    return Piece(PLAY_WIDTH // 2 - 2, 0, shape, color)

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (WINDOW_WIDTH / 2 - label.get_width() / 2, WINDOW_HEIGHT / 2 - label.get_height() / 2))

def draw_grid(surface, grid):
    for i in range(PLAY_HEIGHT):
        pygame.draw.line(surface, GRAY, (0, i*BLOCK_SIZE), (300, i*BLOCK_SIZE))
    for j in range(PLAY_WIDTH):
        pygame.draw.line(surface, GRAY, (j*BLOCK_SIZE, 0), (j*BLOCK_SIZE, 600))
    for i in range(PLAY_HEIGHT):
        for j in range(PLAY_WIDTH):
            pygame.draw.rect(surface, grid[i][j], (j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

def clear_rows(grid, locked):
    cleared = 0
    for i in range(PLAY_HEIGHT-1, -1, -1):
        if BLACK not in grid[i]:
            cleared += 1
            for j in range(i, 0, -1):
                grid[j] = grid[j-1]
            grid[0] = [BLACK for _ in range(PLAY_WIDTH)]
    if cleared > 0:
        locked.clear()
        for i in range(PLAY_HEIGHT):
            for j in range(PLAY_WIDTH):
                if grid[i][j] != BLACK:
                    locked[(j, i)] = grid[i][j]
    return cleared

def draw_next_piece(surface, piece):
    font = pygame.font.SysFont("comicsans", 25)
    label = font.render("Next Piece:", 1, WHITE)
    sx = 320
    sy = 100
    surface.blit(label, (sx, sy))
    fmt = piece.shape[piece.rotation]
    for (x, y) in fmt:
        pygame.draw.rect(surface, piece.color, (sx + x*BLOCK_SIZE, sy + 40 + y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

def draw_window(surface, grid, score, next_piece):
    surface.fill(BLACK)
    font = pygame.font.SysFont("comicsans", 40)
    label = font.render("TETRIS", 1, WHITE)
    surface.blit(label, (150 - (label.get_width()//2), 10))
    font = pygame.font.SysFont("comicsans", 25)
    score_label = font.render(f"Score: {score}", 1, WHITE)
    surface.blit(score_label, (320, 50))
    draw_grid(surface, grid)
    draw_next_piece(surface, next_piece)
    pygame.display.update()

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    locked_positions = {}
    grid = create_grid(locked_positions)
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.5
    level_time = 0
    score = 0
    running = True
    while running:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()
        if level_time/1000 > 20:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                for (x, y) in current_piece.image():
                    locked_positions[(current_piece.x + x, current_piece.y + y)] = current_piece.color
                current_piece = next_piece
                next_piece = get_shape()
                cleared = clear_rows(grid, locked_positions)
                score += [0, 40, 100, 300, 1200][min(cleared, 4)]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = (current_piece.rotation - 1) % len(current_piece.shape)
        shape_pos = [(current_piece.x + x, current_piece.y + y) for (x, y) in current_piece.image()]
        for (x, y) in shape_pos:
            if y > -1:
                grid[y][x] = current_piece.color
        if check_lost(locked_positions):
            draw_text_middle(screen, "YOU LOST!", 40, WHITE)
            pygame.display.update()
            pygame.time.delay(2000)
            running = False
        draw_window(screen, grid, score, next_piece)
    pygame.quit()

def main_menu():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    run = True
    while run:
        screen.fill(BLACK)
        draw_text_middle(screen, "Press Any Key to Play", 30, WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()

if __name__ == "__main__":
    main_menu()