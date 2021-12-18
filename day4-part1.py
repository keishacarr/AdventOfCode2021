import numpy as np

# read in draw numbers

# read in/create boards; store listBoards
class Board:
    x = 5

no_winner = True
while no_winner:
    # while loop through listBoards
        # mark board with drawn number
        # check board
    # see if any boards are ready; if a Board is ready, calculate final value. if not, loop again.
    no_winner = False

def calc_winner (board):
    #find unmarked
    unmarked_sum = 0
    for row in range (0, 5):
        for col in range (0, 5):
            if board[row][col][1] == 'u':
                unmarked_sum += board[row][col][0]
    # return sum
    pass

def mark_board (board, drawn):
    for row in range (0, 5):
        for col in range (0, 5):
            if board[row][col] == drawn:
                board[row][col][1] = 'm'
    pass

def check_board (board):
    for i in range (0, 5):
        if (check_rowcol(board[:,i])):
            print("success!")
            break

def check_rowcol (rowcol):
    num_marked = 0
    for i in range(0, 5):
        if rowcol[i][1] == 'm':
            num_marked += 1
    if num_marked == 5:
        return True
    elif:
        return False