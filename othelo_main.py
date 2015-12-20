#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2
import perspective as pers
import serial_send as send
import my_othelo_ai as ai
import inverse_kinematics as ik

WIN_SIZE = 600
WHITE = -1
BLANK = 0
BLACK = 1

#position of othelo board
X1 = -120
Y1 = 330
X2 = 120
Y2 = 330

#arms' length
L1 = 180
L2 = 150
            
def main():
    cap_num = 0
    dev = '/dev/ttyACM0'
    if len(sys.argv) > 1:
        cap_num = int(sys.argv[1])
    if len(sys.argv) > 2:
        dev = sys.argv[2]
        
    board = np.zeros([6, 6])
    phase = 0
    cv2.namedWindow('src')
    cv2.namedWindow('adjust_color')
    cv2.namedWindow('adjust_threshold')
    
    cap = cv2.VideoCapture(cap_num)
    edge_list = pers.Edge_list()
    cv2.setMouseCallback('src', edge_list.get_edgepos)
    cv2.createTrackbar('H-min', 'adjust_color', 0, 180, pers.nothing)
    cv2.createTrackbar('H-max', 'adjust_color', 0, 180, pers.nothing)
    cv2.createTrackbar('S-min', 'adjust_color', 0, 255, pers.nothing)
    cv2.createTrackbar('S-max', 'adjust_color', 0, 255, pers.nothing)
    cv2.createTrackbar('threshold', 'adjust_threshold', 0, 255, pers.nothing)
    h_min = h_max = s_min = s_max = threshold = 0

    while True:
        ret, src = cap.read()
        
        if len(edge_list.edge_list) < 4:
            phase = 1
            cv2.imshow('src', src)
            h_min = cv2.getTrackbarPos('H-min', 'adjust_color')
            h_max = cv2.getTrackbarPos('H-max', 'adjust_color')
            s_min = cv2.getTrackbarPos('S-min', 'adjust_color')
            s_max = cv2.getTrackbarPos('S-max', 'adjust_color')
            threshold = cv2.getTrackbarPos('threshold', 'adjust_threshold')
            adjust_color = pers.make_hsv(src, h_min, h_max, s_min, s_max)
            adjust_threshold = pers.make_thresh(src, threshold)
            cv2.imshow('adjust_color', adjust_color)
            cv2.imshow('adjust_threshold', adjust_threshold)
            
        else:
            phase = 2
            #h_min = 54
            #h_max = 87
            #s_min = 90
            #s_max = 164
            #threshold = 118
            cv2.destroyWindow('adjust_color')
            cv2.destroyWindow('adjust_threshold')
            adjusted_color = pers.make_hsv(src, h_min, h_max, s_min, s_max)
            adjusted_threshold = pers.make_thresh(src, threshold)

            dst = pers.trans_pers(src, edge_list, WIN_SIZE, WIN_SIZE)
            adjusted_color = pers.trans_pers(adjusted_color, edge_list, WIN_SIZE, WIN_SIZE)
            adjusted_threshold = pers.trans_pers(adjusted_threshold, edge_list, WIN_SIZE, WIN_SIZE)
            
            cv2.imshow('src', src)
            cv2.imshow('adjusted_color', adjusted_color)
            cv2.imshow('adjusted_threshold', adjusted_threshold)
            cv2.imshow('dst', dst)
            
        ch = cv2.waitKey(1)
        if ch == ord('q'):
            break
        elif ch == ord(' ') and phase == 2:
            pers.get_board_info(board, adjusted_color, adjusted_threshold, 10, 10)
            pers.print_board(board)
            next_pos = ai.decide_next_pos(board)
            print next_pos
            #reverse_pos = pos = ai.decide_reverse_pos(board, next_pos)
            #pos.insert(0, next_pos)
            #print pos
            #arg = ik.pos_to_arg(pos) #パターン2
            arg = ik.pos_to_arg([next_pos]) #パターン1
            print arg
            send.send_num2(arg, dev)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
