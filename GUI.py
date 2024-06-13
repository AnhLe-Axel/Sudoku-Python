import pygame
from Module import *
from sys import exit

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

board_width = 450
size = 9

# ----- Main Code -----
pygame.init()
screen = pygame.display.set_mode((board_width, board_width))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)
grid = Grid(size, board_width, board, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            grid.click(event.pos)

    screen.fill("White")
    grid.draw(font)

    pygame.display.update()
    clock.tick(60)
