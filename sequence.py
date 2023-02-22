#!/usr/bin/python
from random import random
from time import sleep
from functools import partial
from gpiozero import LED, Button
from signal import pause
import sys

t=.2
d=.05
# the ones commented out don't seem to be wired properly.

leds = {
   "r0": 4,
    "y0": 17,
    "g0": 18,
    "r1": 23,
    "y1": 24,
    "g1": 25,
    "b0": 27,
    "w0": 22,
    "cf": 26,
    "b1": 5,

#    "w1": 6,
#    "rgbr": 12,
#    "rgbg": 13,
#    "rgbb": 19,

   "cs": 20}
buttons = {
    "r": 2,
    "g": 3,
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
    global d
    t = t + d
    print(t)

def less():
    global t
    global d
    if t <= .1:
        return
    else:
        t = t - d
    print(t)


buttons['r'].when_pressed = lambda: more()
buttons['y'].when_pressed = lambda: less()



while(True):
    for (k,v) in leds.items():
        v.on()
        sleep(t)
        v.off()





