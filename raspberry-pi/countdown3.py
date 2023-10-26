#type:ignore

import board
import time
import digitalio

button = digitalio.DigitalInOut(board.GP28)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # makes it so that when the button is not being pushed it outputs a TRUE value and when it is pushed it outputs a FALSE value.
abort = 0 # this will be used to help with the spicy version of the assignment.

red = digitalio.DigitalInOut(board.GP15)
red.direction = digitalio.Direction.OUTPUT

green = digitalio.DigitalInOut(board.GP16)
green.direction = digitalio.Direction.OUTPUT
while True:
    if button.value == False: #if the button is pushed
        if abort == 0: # if the countdown is not active
            for x in range(11):
                if x<10:
                    if abort == 1 and button.value == False: # if the button is pushed during the countdown print ABORT
                        print('ABORT')
                        time.sleep(.1)
                        break # stops the loop
                    print(10-x)
                    red.value = True
                    time.sleep(.1)
                    red.value = False
                    green.value = False
                    time.sleep(.9)
                    abort = 1 # this is used to check if the countdown is active
                else:
                    print('liftoff!')
                    while True:
                        abort = 1 # makes it so that you can't abort the countdown after it already finished
                        green.value = True
    else:
        abort = 0 # this is just to make it so the abort value doesn't stay at one