#type:ignore

import board
import time
import digitalio

red = digitalio.DigitalInOut(board.GP15) #Lets the Pico know that changing the value of red means changing the power going to pin 15
red.direction = digitalio.Direction.OUTPUT #Lets the Pico know that it is sending data out to 'red' and not recieving data

green = digitalio.DigitalInOut(board.GP16) #Same thing as line 6, but with pin 16 instead.
green.direction = digitalio.Direction.OUTPUT
for x in range(11):
    if x<10:
        red.value = False #Turns off the red LED
        green.value = False #Turns off the green LED
        time.sleep(.9) 
        print(10-x)
        red.value = True #Turns on the red LED for
        time.sleep(.1)   #.1 second
    else:
        print('liftoff!')
        while True: #Makes it so the green LED stays on until the code gets reset
            green.value = True
            red.value = False