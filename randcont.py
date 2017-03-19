#!/usr/bin/python
from random import random
from time import sleep
from functools import partial
from gpiozero import LED, Button
from signal import pause
import sys

t=.5
# the ones commented out don't seem to be wired properly.

leds = {
    "r0": 4,
    "y0": 17,
    "g0": 18,
    "b0": 27,
    "w0": 22,
    "r1": 23,
    "y1": 24,
    "g1": 25,
    "b1": 5,
#    "w1": 6,
#    "rgbr": 12,
#    "rgbg": 13,
#    "rgbb": 19,
    "cf": 26,
    "cs": 20}

buttons = {
    "r": 2,
#    "g": 3,
    "w": 14,
    "y": 15,
#    "ml": 10,
#    "mr": 9,
    "sl": 11,
    "sr": 8}

for (k,v) in leds.items():
    leds[k] = LED(v)

for (k,v) in buttons.items():
    buttons[k] = Button(v)

def more():
    global t
    t = t + .15

def less():
    global t
    if t <= .15:
        return
    else:
        t = t - .15


buttons['r'].when_pressed = lambda: more()
buttons['y'].when_pressed = lambda: less()



while(True):
    for (k,v) in leds.items():
        if random() > 0.80:
            v.on()
        else:
            v.off()
    sleep(t)





