#type:ignore

import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

button = digitalio.DigitalInOut(board.GP28)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
abort = 0

pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0
red = digitalio.DigitalInOut(board.GP15)
red.direction = digitalio.Direction.OUTPUT

green = digitalio.DigitalInOut(board.GP16)
green.direction = digitalio.Direction.OUTPUT

servo1.angle=0
time.sleep(2)
servo1.angle=180
time.sleep(2)

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
                        servo1.angle = 180
    else:
        abort = 0


# spicy version
#type:ignore
#
#import board
#import time
#import digitalio
#import pwmio
#from adafruit_motor import servo
#
#button = digitalio.DigitalInOut(board.GP28)
#button.direction = digitalio.Direction.INPUT
#button.pull = digitalio.Pull.UP
#abort = 0
#
#pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
#servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
#
#red = digitalio.DigitalInOut(board.GP15)
#red.direction = digitalio.Direction.OUTPUT
#
#green = digitalio.DigitalInOut(board.GP16)
#green.direction = digitalio.Direction.OUTPUT
#servo1.angle = 0
#startServoSweep = 0
#while True:
#    if startServoSweep == 1:
#            if servo1.angle<=1:
#                servo1.angle += 6
#                time.sleep(.1)
#    if button.value == False:
#        if abort == 0:
#            for x in range(11):
#                if x<10:
#                    if abort == 1 and button.value == False:
#                        print('ABORT')
#                        time.sleep(.1)
#                        startServoSweep = 0
#                        servo1.angle = 0
#                        break
#                    if x >= 7:
#                        startServoSweep = 1
#                    print(10-x)
#                    red.value = True
#                    time.sleep(.1)
#                    red.value = False
#                    green.value = False
#                    time.sleep(.9)
#                    abort = 1
#                    
#                else:
#                    print('liftoff!')
#                    while True:
#                        abort = 1
#                        green.value = True
#        
#    else:
#        abort = 0