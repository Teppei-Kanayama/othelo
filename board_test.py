import numpy as np
import my_othelo_ai as ai

board = np.zeros([8, 8]).astype(np.int8)
board[3][3] = board[3][4] = board[5,3] = board[5,4] = 1
board[4][3] = board[4][4] = board[4][5] = board[3, 6] = board[2, 3] = board[3, 5] = -1
print board

next_pos =  ai.decide_next_pos(board)
print next_pos
print ai.decide_reverse_pos(board, next_pos) 
