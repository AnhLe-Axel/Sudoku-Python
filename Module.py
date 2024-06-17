import pygame
import copy

class Square:
    def __init__(self, row, col, value, width):
        self.row = row
        self.col = col
        self.value = value
        self.width = width
        self.selected = False
        self.border_rect = pygame.Surface((width, width)).get_rect(center=(col*width + width/2, row*width + width/2))

    def select(self):
        if self.selected == False: self.selected = True
    
    def de_select(self):
        if self.selected == True: self.selected = False

    def draw(self, font, surface):
        text = font.render("" if self.value == 0 else str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.col*self.width + self.width/2, self.row*self.width + self.width/2))
        surface.blit(text, text_rect)

        if self.selected:
            pygame.draw.rect(surface, "Green", self.border_rect, 3)
    
class Grid:
    def __init__(self, size, width, board, surface):
        self.size = size
        self.width = width
        self.board = board
        self.surface = surface
        self.selected_square = None
        self.squares = [[Square(i, j, board[i][j], width/size) for j in range(size)] for i in range(size)]
        self.solution = copy.deepcopy(board)
        self.solve(self.solution)

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
        valid = False
        for i in range(self.size):
            for j in range(self.size):
                if self.squares[i][j].value == 0:
                    if self.squares[i][j].border_rect.collidepoint(mouse_pos):
                        self.squares[i][j].select()
                        self.selected_square = self.squares[i][j]
                        valid = True
                    else:
                        self.squares[i][j].de_select()
        if not valid:
            self.selected_square = None
        return valid
    
    def write(self, num):
        sel_row = self.selected_square.row
        sel_col = self.selected_square.col
        if self.selected_square is not None and self.solution[sel_row][sel_col] == num:
            self.squares[sel_row][sel_col].value = num
            self.squares[sel_row][sel_col].de_select()
            return True
        return False

    def is_valid(self, bo, pos, num):
        """
        Return True if the attempted move is valid
        """

        for i in range(9):
            if bo[pos[0]][i] == num:
                return False
        
        for i in range(9):
            if bo[i][pos[1]] == num:
                return False
            
        box_x = pos[0]//3
        box_y = pos[1]//3

        for i in range (box_x*3, box_x*3 + 3):
            for j in range(box_y*3, box_y*3 + 3):
                if bo[i][j] == num:
                    return False
        
        return True

    def find_empty(self, bo):
        """
        Find and return an empty position in the board
        """

        for i in range(self.size):
            for j in range(self.size):
                if bo[i][j] == 0:
                    return (i,j)

        return None

    def solve(self, bo):
        pos = self.find_empty(bo)
        if pos is None:
            return True
        
        for i in range(1,10):
            if self.is_valid(bo, pos, i):
                bo[pos[0]][pos[1]] = i
                temp = copy.deepcopy(bo)
                if self.solve(bo) == True:
                    return True
                else:
                    for i in range(9):
                        for j in range(9):
                            bo[i][j] = temp[i][j]
        
        return False
    
    def print_board(self, bo):
        """
        prints the board
        :param bo: 2d List of ints
        :return: None
        """
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - -")
            for j in range(len(bo[0])):
                if j % 3 == 0:
                    print(" | ",end="")

                if j == 8:
                    print(bo[i][j], end="\n")
                else:
                    print(str(bo[i][j]) + " ", end="")
        
