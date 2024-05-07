import copy

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

# domain = [[0] * 9 for i in range(9)]
# for i in range(9):
#     for j in range(9):
#         if board[i][j] == 0:
#             domain[i][j] = [x for x in range(1,10)]
#         else:
#             domain[i][j] = board[i][j]

def is_valid(bo, pos, num):
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

def find_empty(bo):
    """
    Find and return an empty position in the board
    """

    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i,j)

    return None

def solve(bo):
    pos = find_empty(bo)
    if pos is None:
        return True
    
    for i in range(1,10):
        if is_valid(bo, pos, i):
            bo[pos[0]][pos[1]] = i
            temp = copy.deepcopy(bo)
            if solve(bo) == True:
                return True
            else:
                for i in range(9):
                    for j in range(9):
                        bo[i][j] = temp[i][j]
    
    return False

def print_board(bo):
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

print(solve(board))
print_board(board)
