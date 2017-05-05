import serial
import json
import time
import sys

ser = serial.Serial(sys.argv[1], 115200)
skip_head = 10
i = 0

while True:
    line = ser.readline().strip().split(';')
    if i < skip_head:
        i += 1
        continue
    if len(line) != 16:
	continue

    print line[3]
