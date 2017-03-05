#!/usr/bin/python
from gpiozero import LED, Button
from signal import pause

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
    "ml": 10,
    "mr": 9,
    "sl": 11,
    "sr": 8}

for (k,v) in leds.items():
    leds[k] = LED(v)

for (k,v) in buttons.items():
    buttons[k] = Button(v)

    
while True:
    for l,v in leds.items():
        v.on()
        print l
        raw_input()
        v.off()
