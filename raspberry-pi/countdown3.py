#type:ignore

import board
import time
import digitalio

button = digitalio.DigitalInOut(board.GP28)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
abort = 0

red = digitalio.DigitalInOut(board.GP15)
red.direction = digitalio.Direction.OUTPUT

green = digitalio.DigitalInOut(board.GP16)
green.direction = digitalio.Direction.OUTPUT
while True:
    if button.value == False:
        if abort == 0:
            for x in range(11):
                if x<10:
                    if abort == 1 and button.value == False:
                        print('ABORT')
                        time.sleep(.1)
                        break
                    print(10-x)
                    red.value = True
                    time.sleep(.1)
                    red.value = False
                    green.value = False
                    time.sleep(.9)
                    abort = 1
                else:
                    print('liftoff!')
                    while True:
                        abort = 1
                        green.value = True
    else:
        abort = 0