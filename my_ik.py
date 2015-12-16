#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *
import numpy as np

def inverse_kinematics(x, y, ox, oy, l1, l2):
    #(ox, oy) アームの原点(グローバル座標系)
    #(x, y) アームのエンドエフェクターの座標(グローバル座標系)
    #l1, l2 アームの長さ
    #グローバル座標系はz軸が鉛直上向き、オセロ座標系はz軸が鉛直下向き
    j_min = 100.
    ans = [0, 0]
    for alpha in range(180):
        for beta in range(180):
            j1 = ox - x + l1 * cos(alpha / 180. * pi) + l2 * cos(beta / 180. * pi)
            j2 = oy - y + l1 * sin(alpha / 180. * pi) + l2 * sin(beta / 180. * pi)
            j = pow(j1, 2) + pow(j2, 2)
            if j < j_min:
                j_min = j
                ans = [int(alpha),int(beta)]
    return ans

def calc_coord(x, y, x1, y1, x2, y2): #グローバル座標系におけるオセロの端点(x1, y1), (x2, y2)をもとに、オセロ座標系(x, y)(x = 0~7, y = 0~7)をグローバル座標系に変換
    e1 = np.array([x2 - x1, y2 - y1]) / 8
    e2 = np.array([[0, 1], [-1, 0]]).dot(e1) / 8
    #return np.array([x1, y1]) + (x + 0.5) * e1 + (y + 0.5) * e2
    return np.array([x1, y1]) + (y + 0.5) * e1 + (x + 0.5) * e2  
    
def pos_to_arg(pos_list, x1, y1, x2, y2, l1, l2): #グローバル座標系の原点はアームの原点に一致させておく
    ans = []
    for pos in pos_list:
        tmp = calc_coord(pos[0], pos[1], x1, y1, x2, y2)
        ans.append(inverse_kinematics(tmp[0], tmp[1], 0, 0, l1, l2))
    return ans

#print calc_coord(0, 0, 0, 10, 10, 10)
#print inverse_kinematics(0, 20, 0, 0, 10, 10)
