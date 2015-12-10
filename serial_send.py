# -*- coding: utf-8 -*-
import serial

def send_num(num1, num2, dev = '/dev/ttyACM0', baudrate = 9600):
    num = num1 + num2
    ser = serial.Serial(dev, baudrate)
    num_list = list(num)
    for c in num_list:
        ser.write(c)
    ser.close()

send_num('035', '023')
