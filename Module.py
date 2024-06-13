import pygame
import copy

class Square:
    def __init__(self, row, col, value, width):
        self.row = row
        self.col = col
        self.value = value
        self.width = width
        self.selected = False
        self.text_rect = None
        self.border_rect = pygame.Surface((width, width)).get_rect(center=(row*width + width/2, col*width + width/2))

    def select(self):
        if self.selected == False: self.selected = True
    
    def de_select(self):
        if self.selected == True: self.selected = False

    def draw(self, font, surface):
        text = font.render("" if self.value == 0 else str(self.value), True, (0, 0, 0))
        self.text_rect = text.get_rect(center=(self.row*self.width + self.width/2, self.col*self.width + self.width/2))
        surface.blit(text, self.text_rect)

        if self.selected:
            pygame.draw.rect(surface, "Green", self.border_rect, 3)
    
class Grid:
    def __init__(self, size, width, board, surface):
        self.size = size
        self.width = width
        self.board = board
        self.surface = surface
        self.squares = [[Square(i, j, board[i][j], width/size) for j in range(size)] for i in range(size)]
        self.temp = copy.deepcopy(board)

    def draw(self, font):
        # Draw the grid
        gap = self.width/self.size
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.surface, (0, 0, 0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(self.surface, (0, 0, 0), (i * gap, 0), (i * gap, self.width), thick)

        # Fill in the number
        for i in range(self.size):
            for j in range(self.size):
                self.squares[i][j].draw(font, self.surface)

    def click(self, mouse_pos):
        for i in range(self.size):
            for j in range(self.size):
                if self.squares[i][j].value == 0:
                    if self.squares[i][j].border_rect.collidepoint(mouse_pos):
                        self.squares[i][j].select()
                    else:
                        self.squares[i][j].de_select()
