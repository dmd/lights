#!/usr/bin/python
from time import sleep
from functools import partial
from gpiozero import LED, Button
from signal import pause
import sys


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
    "g": 3,
    "w": 14,
    "y": 15,
#    "ml": 10,
    "mr": 9,
    "sl": 11,
    "sr": 8}

for (k,v) in leds.items():
    leds[k] = LED(v)

for (k,v) in buttons.items():
    buttons[k] = Button(v)


def ontwo(onled,blinkled):
    leds[onled].on()
    leds[blinkled].blink(on_time=.25,off_time=.25)

def offtwo(onled,blinkled):
    leds[onled].off()
    leds[blinkled].off()

def onoff(b, l1, l2):
    buttons[b].when_pressed = lambda l1=l1, l2=l2: ontwo(l1, l2)
    buttons[b].when_released = lambda l1=l1, l2=l2: offtwo(l1, l2)

def allon():
    for (k,v) in leds.items():
        v.on()

def alloff():
    for (k,v) in leds.items():
        v.off()

        
onoff('r','r0', 'r1')
onoff('w','cf', 'w0')
onoff('y','y0', 'y1')
onoff('g','g0', 'g1')
#onoff('sl','g0', 'g1')
#onoff('sr','b0', 'b1')

buttons['sr'].when_pressed = allon
buttons['sr'].when_released = alloff


pause()




