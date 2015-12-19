#!/usr/bin/env python
import numpy as np
WHITE = -1
BLANK = 0
BLACK = 1

class Board: # represent reversi board
    def __init__(self, board, current = WHITE):
        self.board = board
        self.current = current # current player
        
    def validate_range(self, x, y): # validate input range
        if x < 0 or x > 5 or y < 0 or y > 5:
            return False
        return True

    def validate_input(self, x, y): # validate input
        if not self.validate_range(x, y):
            return False
        if not self.board[x][y] == BLANK:
            return False
        elif not self.can_reverse(x, y):
            return False
        return True

    def can_reverse(self, x, y):
        storex, storey = x, y
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if not self.validate_range(x + dx, y + dy):
                    continue
                if self.board[x + dx][y + dy] == -self.current:
                    if (self.can_reverse_one_dir(x + dx, y + dy, dx, dy) != False):
                        return True
        return False
    
    def can_reverse_one_dir(self, x, y, dx, dy):
        reverse_list = []
        while self.validate_range(x, y):
            if self.board[x][y] == BLANK:
                return False
            elif self.board[x][y] == -self.current:
                reverse_list.append([x, y])
                x += dx
                y += dy
                continue
            elif self.board[x][y] == self.current:
                return reverse_list
        return False

def find_next_pos(board):
    now_board = Board(board)
    next_pos_list = []
    for y in range(6):
        for x in range(6):
            if now_board.validate_input(x, y):
                next_pos_list.append([x, y])
    return next_pos_list

def decide_next_pos(board):
    
    next_pos_list = find_next_pos(board)
    if next_pos_list == []:
        return [3, 3]
    evaluation_value = np.zeros(len(next_pos_list))
    for i, pos in enumerate(next_pos_list):
        evaluation_value[i] = evaluation_function(board, pos)
    return next_pos_list[np.argmax(evaluation_value)]

def evaluation_function(board, one_of_pos):
    evaluation_value = 0
    reverse_list = decide_reverse_pos(board, one_of_pos)
    reverse_list.append(one_of_pos)
    for pos in reverse_list:
        if pos == [0, 0] or pos == [0, 5] or pos == [5, 0] or pos == [5, 5]:
            evaluation_value += 30
        elif pos == [1, 0] or pos == [0, 1] or pos == [0, 4] or pos == [4, 0] or pos == [1, 5] or pos == [5, 1] or pos == [4, 5] or pos == [5, 4]:
            evaluation_value -= 12
        elif pos == [1, 1] or pos == [1, 4] or pos == [4, 1] or pos == [4, 4]:
            evaluation_value -=15
        else:
            evaluation_value -= 1
    return evaluation_value
         

def decide_reverse_pos(board, next_pos):
    reverse_list = []
    now_board = Board(board)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            tmp = now_board.can_reverse_one_dir(next_pos[0] + dx, next_pos[1] + dy, dx, dy)
            if tmp != False:
                reverse_list.extend(tmp)
    return reverse_list
