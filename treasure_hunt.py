import serial
import json
import time
import sys

import RPi.GPIO as GPIO

ser = serial.Serial(sys.argv[1], 115200)
skip_head = 10
i = 0

R_PIN = 13
G_PIN = 5
B_PIN = 21

CLOSE = {
    R_PIN: GPIO.HIGH,
    G_PIN: GPIO.HIGH,
    B_PIN: GPIO.HIGH,
}
NEAR = {
    R_PIN: GPIO.LOW,
    G_PIN: GPIO.HIGH,
    B_PIN: GPIO.HIGH,
}
FAR = {
    R_PIN: GPIO.LOW,
    G_PIN: GPIO.HIGH,
    B_PIN: GPIO.LOW,
}
LOST = {
    R_PIN: GPIO.LOW,
    G_PIN: GPIO.LOW,
    B_PIN: GPIO.LOW,
}

def change_PIN_status(cond):
    for pin, hl in cond.iteritems():
        GPIO.output(pin, hl)        

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)

while True:
    line = ser.readline().strip().split(';')
    if i < skip_head:
        i += 1
        continue
    if len(line) != 16:
	continue
    distance = int(line[3])

    print distance
    if distance > 140:
        change_PIN_status(CLOSE)
    elif distance > 90:
        change_PIN_status(NEAR)
    elif distance > 45:
        change_PIN_status(FAR)
    else:
        change_PIN_status(LOST)
