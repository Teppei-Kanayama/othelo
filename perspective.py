# -*- coding: utf-8 -*-

import numpy as np
import cv2
import sys
import my_othelo_ai as ai

WHITE = -1
BLANK = 0
BLACK = 1

def nothing(x):
    pass

class Edge_list:
    def __init__(self):
        self.edge_list = []
    def get_edgepos(self, event, x, y, flags, param):
        if len(self.edge_list) < 4:
            if event == cv2.EVENT_LBUTTONDOWN:
                self.edge_list.append([x, y])
                print x, y

def get_average(img, center_pos, dx_max, dy_max):
    tmp = 0
    for dy in range(-dy_max+1, dy_max):
        for dx in range(-dx_max+1, dx_max):
           tmp += img[center_pos[0] + dx, center_pos[1] + dy]
    ave = tmp / ((dx_max * 2 - 1) * (dy_max * 2 - 1))
    return ave     

def make_hsv(img_color, h_min, h_max, s_min, s_max):
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
    img_h = img_hsv[:, :, 0]
    img_s = img_hsv[:, :, 1]
    return (255 * (h_min < img_h) * (img_h < h_max) * (s_min < img_s) * (img_s < s_max)).astype(np.uint8)

def make_thresh(img_color, threshold):
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    ret, img_thresh = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
    return img_thresh

def trans_pers(img, edge_list, win_x, win_y):
    pts1 = np.float32(edge_list.edge_list)
    pts2 = np.float32([[0, 0], [win_x, 0], [win_x, win_y], [0, win_y]])
    psp_mat = cv2.getPerspectiveTransform(pts1, pts2)
    return cv2.warpPerspective(img, psp_mat, (win_x, win_y))
    
def get_board_info(board, adjusted_color, adjusted_threshold, dx, dy): 
    x = 50
    y = 50
    for j in range(6):
        for i in range(6):
            if get_average(adjusted_threshold, (x, y), dx, dy) > 200:
                board[i][j] = WHITE
            elif get_average(adjusted_color, (x, y), dx, dy) > 200:
                board[i][j] = BLANK
            else:
                board[i][j] = BLACK
            x += 100
        x = 50
        y += 100

def print_board(board):
    for j in range(6):
        for i in range(6):
            if (board[j][i] == BLANK):
                sys.stdout.write('.  ')
            elif (board[j][i] == WHITE):
                sys.stdout.write('o  ')
            elif (board[j][i] == BLACK):
                sys.stdout.write('*  ')
        print '\n'
    print "-------------------------"
    
