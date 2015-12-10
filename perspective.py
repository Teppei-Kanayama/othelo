# -*- coding: utf-8 -*-

import numpy as np
import cv2
import sys
import my_othelo_ai as ai

WIN_SIZE = 800
edge_list = []
WHITE = -1
BLANK = 0
BLACK = 1

def nothing(x):
    pass

def get_edgepos(event, x, y, flags, param):
    if len(edge_list) < 4:
        if event == cv2.EVENT_LBUTTONDOWN:
            edge_list.append([x, y])
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

def trans_pers(img, win_x = WIN_SIZE, win_y = WIN_SIZE):
    pts1 = np.float32(edge_list)
    pts2 = np.float32([[0, 0], [win_x, 0], [win_x, win_y], [0, win_y]])
    psp_mat = cv2.getPerspectiveTransform(pts1, pts2)
    return cv2.warpPerspective(img, psp_mat, (win_x, win_y))
    
def get_board_info(board, adjusted_color, adjusted_threshold, dx, dy): 
    x = 50
    y = 50
    for j in range(8):
        for i in range(8):
            #cv2.circle(dst, (x, y), 5, (255, 0, 0), -1)
            if get_average(adjusted_color, (x, y), dx, dy) > 200:
                board[i][j] = BLANK
            elif get_average(adjusted_threshold, (x, y), dx, dy) > 200:
                board[i][j] = WHITE
            elif get_average(adjusted_threshold, (x, y), dx, dy) < 50:
                board[i][j] = BLACK
            x += 100
        x = 50
        y += 100

def print_board(board):
    for j in range(8):
        for i in range(8):
            if (board[j][i] == BLANK):
                sys.stdout.write('.  ')
            elif (board[j][i] == WHITE):
                sys.stdout.write('o  ')
            elif (board[j][i] == BLACK):
                sys.stdout.write('*  ')
        print '\n'
    print "-------------------------"
    
def main():
    board = np.zeros([8, 8])
    phase = 0
    cv2.namedWindow('src')
    cv2.namedWindow('adjust_color')
    cv2.namedWindow('adjust_threshold')
    
    cap = cv2.VideoCapture(0)
    cv2.setMouseCallback('src', get_edgepos)
    cv2.createTrackbar('H-min', 'adjust_color', 0, 180, nothing)
    cv2.createTrackbar('H-max', 'adjust_color', 0, 180, nothing)
    cv2.createTrackbar('S-min', 'adjust_color', 0, 255, nothing)
    cv2.createTrackbar('S-max', 'adjust_color', 0, 255, nothing)
    cv2.createTrackbar('threshold', 'adjust_threshold', 0, 255, nothing)
    h_min = h_max = s_min = s_max = threshold = 0

    while True:
        ret, src = cap.read()
        
        if len(edge_list) < 4:
            phase = 1
            cv2.imshow('src', src)
            h_min = cv2.getTrackbarPos('H-min', 'adjust_color')
            h_max = cv2.getTrackbarPos('H-max', 'adjust_color')
            s_min = cv2.getTrackbarPos('S-min', 'adjust_color')
            s_max = cv2.getTrackbarPos('S-max', 'adjust_color')
            threshold = cv2.getTrackbarPos('threshold', 'adjust_threshold')
            adjust_color = make_hsv(src, h_min, h_max, s_min, s_max)
            adjust_threshold = make_thresh(src, threshold)
            cv2.imshow('adjust_color', adjust_color)
            cv2.imshow('adjust_threshold', adjust_threshold)
            
        else:
            phase = 2
            cv2.destroyWindow('adjust_color')
            cv2.destroyWindow('adjust_threshold')
            adjusted_color = make_hsv(src, h_min, h_max, s_min, s_max)
            adjusted_threshold = make_thresh(src, threshold)

            dst = trans_pers(src)
            adjusted_color = trans_pers(adjusted_color)
            adjusted_threshold = trans_pers(adjusted_threshold)
            
            cv2.imshow('src', src)
            cv2.imshow('adjusted_color', adjusted_color)
            cv2.imshow('adjusted_threshold', adjusted_threshold)
            cv2.imshow('dst', dst)
            
        ch = cv2.waitKey(1)
        if ch == ord('q'):
            break
        elif ch == ord(' ') and phase == 2:
            get_board_info(board, adjusted_color, adjusted_threshold, 10, 10)
            print_board(board)
            next_pos = ai.decide_next_pos(board)
            reverse_pos = ai.decide_reverse_pos(board, next_pos)
            print next_pos
            print reverse_pos
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
