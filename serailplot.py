import logging
import threading
import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse
def initSerial(port,baudrate):
    # ポートの設定
    COM=port      #通信ポート
    bitRate=baudrate   #通信速度
    ser = serial.Serial(COM, bitRate, timeout=0.1)
    return ser

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-p', '--port', default='/dev/tty.usbmodem11103')
    args.add_argument('-b', '--baudrate', default=115200)
    args = args.parse_args()
    ser = initSerial(args.port,args.baudrate)
    while True:
        data = ser.readline()
        if data != b'':
            line = data.decode('utf-8').rstrip()
            print(line)
        