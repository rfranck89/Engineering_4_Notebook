#type:ignore
import board
import time
import adafruit_mpu6050 #imports the mpu
import busio #imports busio

sda_pin = board.GP26 
scl_pin = board.GP27
i2c = busio.I2C(scl_pin, sda_pin) #lets the pico know that pin 26 is the sda pin and pin 27 is the scl pin.
mpu = adafruit_mpu6050.MPU6050(i2c)
while True:
    print(f'X = {mpu.acceleration[0]}, Y = {mpu.acceleration[1]}, Z = {mpu.acceleration[2]}') #prints the accelerometer's x, y, and z velocity 10 times every second
    time.sleep(.1)