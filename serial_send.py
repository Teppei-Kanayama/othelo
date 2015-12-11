# -*- coding: utf-8 -*-
import serial

def send_num(nums, dev = '/dev/ttyACM0', baudrate = 9600): # nums = [int num1, int num2]
    num_str = ''
    for num in nums:
        if num < 10:
            num_str += '00' + str(num)
        elif num < 100:
            num_str += '0' + str(num)
        else:
            num_str += str(num)
            
    ser = serial.Serial(dev, baudrate)
    num_list = list(num)
    for c in num_list:
        ser.write(c)
    ser.close()

#send_num(35, 23)
