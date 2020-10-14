#!/usr/bin/env python3
import os, sys
import re
import serial
import time


if __name__ == '__main__':
    serialcom = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    serialcom.flush()
    while True:
        if serialcom.in_waiting > 0:
            line = serialcom.readline().decode('utf-8').rstrip()