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
max_live = 3

# ----- Main Code -----
pygame.init()
screen = pygame.display.set_mode((board_width, board_width))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()
font1 = pygame.font.Font(None, 32)
font2 = pygame.font.Font("fonts/CookieCrisp-L36ly.ttf", 40)

game_name_surf = font2.render(f'Sudoku Game', False, (64,64,64))
game_name_rect = game_name_surf.get_rect(center = (board_width/2, board_width/2 - 50))
instruction_surface = font1.render(f'Press space to start the game!', False, (64,64,64))
instruction_rect = instruction_surface.get_rect(center = (board_width/2, board_width/2))
lost_surf = font2.render(f'You lost!', False, (64,64,64))
lost_rect = lost_surf. get_rect(center = (board_width/2, board_width/2 - 50))

game_active = False
selecting = False
curr_live = max_live
lost = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                selecting = grid.click(event.pos)
        
            if event.type == pygame.KEYDOWN:
                if selecting:
                    is_correct = None
                    if event.key == pygame.K_1:
                        is_correct = grid.write(1)
                    elif event.key == pygame.K_2:
                        is_correct = grid.write(2)
                    elif event.key == pygame.K_3:
                        is_correct = grid.write(3)
                    elif event.key == pygame.K_4:
                        is_correct = grid.write(4)
                    elif event.key == pygame.K_5:
                        is_correct = grid.write(5)
                    elif event.key == pygame.K_6:
                        is_correct = grid.write(6)
                    elif event.key == pygame.K_7:
                        is_correct = grid.write(7)
                    elif event.key == pygame.K_8:
                        is_correct = grid.write(8)
                    elif event.key == pygame.K_9:
                        is_correct = grid.write(9)
                    
                    if is_correct != None:
                        if is_correct:
                            pass
                        else:
                            curr_live -= 1
                            if curr_live <= 0:
                                game_active = False
                                lost = True
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    if game_active:
        screen.fill("White")
        grid.draw(font1)
    else:
        screen.fill((94,129,162))
        if lost:
            screen.blit(lost_surf, lost_rect)
        else:
            screen.blit(game_name_surf, game_name_rect)
        screen.blit(instruction_surface, instruction_rect)

        grid = Grid(size, board_width, board, screen)
        curr_live = max_live

    pygame.display.update()
    clock.tick(60)
