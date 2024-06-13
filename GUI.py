import pygame
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
row_num = 9

# Draw grid:
def draw_grid():
    gap = board_width/row_num

    for i in range(row_num):
        if i % 3 == 0 and i != 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i*gap), (board_width, i*gap), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * gap, 0), (i * gap, board_width), thick)

def write_number():
    for i in range(9):
        for j in range(9):
            text = font.render("" if board[i][j] == 0 else str(board[i][j]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(i*50 + 25, j*50 + 25))
            screen.blit(text, text_rect)

# ----- Main Code -----
pygame.init()
screen = pygame.display.set_mode((board_width, board_width))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()

square_surface = pygame.Surface((50, 50)) 
square_surface.fill("White")
font = pygame.font.Font(None, 32)
number_rect_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("White")
    draw_grid()
    write_number()

    pygame.display.update()
    clock.tick(60)