#type:ignore
import board
import time
import digitalio
import adafruit_mpu6050 #imports the mpu
import busio #imports busio
warning = digitalio.DigitalInOut(board.GP16)
warning.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP26 
scl_pin = board.GP27
i2c = busio.I2C(scl_pin, sda_pin) #lets the pico know that pin 26 is the sda pin and pin 27 is the scl pin.
mpu = adafruit_mpu6050.MPU6050(i2c)
while True:
    if mpu.acceleration[2] < 2:
        warning.value = True
    else:
        warning.value = False
    print(f'X = {mpu.acceleration[0]}, Y = {mpu.acceleration[1]}, Z = {mpu.acceleration[2]}') #these two lines of code are kind of useless because the purpose of this assignment is to have the code work without being plugged into the computer, and the computer won't print anything if it isn't connected to the pico.
    time.sleep(.1)