import numpy as np

GRID_R=6
GRID_C=9

def play_board():
    board = np.zeros((GRID_R,GRID_C))
    #board = np.chararray((GRID_R,GRID_C))
    #print(board)
    print(type(board))
    return board

def print_play_board(board):
    print(np.flip(board , 0 ))

play_board()