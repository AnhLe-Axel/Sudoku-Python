import pygame
import copy

class Square:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.selected = False
        self.rect = None

    def select(self):
        if self.selected == False: self.selected = True

    def draw(self, gap, font, surface):
        text = font.render("" if self.value == 0 else str(self.value), True, (0, 0, 0))
        self.rect = text.get_rect(center=(self.row*gap + gap/2, self.col*gap + gap/2))
        surface.blit(text, self.rect)

        if self.selected:
            pygame.draw.rect(surface, "Green", self.rect, 1)
    
class Grid:
    def __init__(self, size, width, board, surface):
        self.size = size
        self.width = width
        self.board = board
        self.surface = surface
        self.squares = [[Square(i, j, board[i][j]) for j in range(size)] for i in range(size)]
        self.temp = copy.deepcopy(board)

    def draw(self, font):
        gap = self.width/self.size
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.surface, (0, 0, 0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(self.surface, (0, 0, 0), (i * gap, 0), (i * gap, self.width), thick)

        for i in range(self.size):
            for j in range(self.size):
                self.squares[i][j].draw(gap, font, self.surface)

