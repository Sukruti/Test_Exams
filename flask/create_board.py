import numpy as np

GRID_R=6
GRID_C=9
def play_board():
    board = np.zeros((GRID_R,GRID_C))
    #board = np.chararray((GRID_R,GRID_C))
    print(board)
    return board

def is_valid_place(board , column):
    print(column)
    if board[GRID_R - 1 ][column]!=0:
        print('This column is full')
    return board[GRID_R - 1 ][column]==0

def get_next_open_row(board ,column):
    for row in range(GRID_R):
        if board[row][column] == 0:
            return row

def place_discs(board ,row, column , discs):
    board[row][column] = discs

def winning_move(board , discs):
    #Horizontal Location
    #All posible starting Positions  , we cannot go 4 location beyond the (GRID_C-3)
    for col in range(GRID_C-3):
        for row in range(GRID_R):
            if board[row][col] == discs and board[row][col+1] == discs and board[row][col+2] == discs and board[row][col+3] == discs:
                return True
    #Vertical Locations
    # All posible starting Positions  , we cannot go 4 location beyond the (GRID_R-3)
    for col in range(GRID_C):
        for row in range(GRID_R-3):
            if board[row][col] == discs and board[row+1][col] == discs and board[row+2][col] == discs and board[row+3][col] == discs:
                return True
    #Diagonal Upward
    for col in range(GRID_C-3):
        for row in range(GRID_R-3):
            if board[row][col] == discs and board[row+1][col+1] == discs and board[row+2][col+2] == discs and board[row+3][col+3] == discs:
                return True
    #Diagonal Downward
    for col in range(GRID_C):
        for row in range(3,GRID_R):
            if board[row][col] == discs and board[row-1][col+1] == discs and board[row-2][col+2] == discs and board[row-3][col+3] == discs:
                return True

def print_play_board(board):
    print(np.flip(board , 0 ))

board= play_board()
game_over = False
turn = 0


while not game_over:
    if turn%2 ==0:
        column = int(input("Make your selection between 1 and 9 (Player 1):"))
        if is_valid_place(board , column-1):
            row = get_next_open_row(board , column-1)
            place_discs(board,row,column-1 ,1)
            turn += 1
            if winning_move(board, 1) :
                print("Player 1 Won the Game...!!!")
                game_over = True

    else:
        column = int(input("Make your selection between 1 and 9 (Player 2):"))
        if is_valid_place(board , column-1):
            row = get_next_open_row(board , column-1)
            place_discs(board,row,column-1 ,2)
            turn += 1
            if winning_move(board, 2) :
                print("Player 2 Won the Game...!!!")
                game_over = True

    print_play_board(board)
