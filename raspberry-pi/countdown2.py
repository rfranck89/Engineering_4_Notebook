#type:ignore

import board
import time
import digitalio
red = digitalio.DigitalInOut(board.GP15)
red.direction = digitalio.Direction.OUTPUT

green = digitalio.DigitalInOut(board.GP16)
green.direction = digitalio.direction.OUTPUT
for x in range(11):
    if x<10:
        red.value = False
        green.value = False
        time.sleep(.9)
        red.value = True
        time.sleep(.1)