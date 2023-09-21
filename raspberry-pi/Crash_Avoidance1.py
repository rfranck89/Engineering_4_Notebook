#type:ignore
import board
import adafruit_mpu6050
import busio

sda_pin = board.GP26
scl_pin = board.GP27
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
while True:
    print(f'dx = {mpu.acceleration[0]}, dy = {mpu.acceleration[1]}, dz = {mpu.acceleration[2]}')