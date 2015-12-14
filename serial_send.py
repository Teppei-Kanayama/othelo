# -*- coding: utf-8 -*-
import serial

def send_num(nums, dev = '/dev/ttyACM0', baudrate = 9600): # nums = [int num1, int num2, int num3, ....]
    num_str = ''
    for num in nums:
        if num < 10:
            num_str += '00' + str(int(num))
        elif num < 100:
            num_str += '0' + str(int(num))
        else:
            num_str += str(int(num))
            
    ser = serial.Serial(dev, baudrate)
    num_list = list(num_str)
    for c in num_list:
        print c
        print type(c)
        ser.write(c)
    ser.close()

def send_num2(nums, dev = '/dev/ttyACM0', baudrate = 9600): # nums = [[int num1, int num2], [int num3, int num4], ....]
    num_str = ''
    for num_pair in nums:
        for num in num_pair:
            if num < 10:
                num_str += '00' + str(int(num))
            elif num < 100:
                num_str += '0' + str(int(num))
            else:
                num_str += str(int(num))
            
    ser = serial.Serial(dev, baudrate)
    num_list = list(num_str)
    for c in num_list:
        print c
        print type(c)
        ser.write(c)
    ser.close()

#send_num(35, 23)
