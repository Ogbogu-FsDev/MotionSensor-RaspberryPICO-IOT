from machine import Pin, PWM, Timer, I2C
import utime
from sequence import *

def LED(): # Onboard LED - Flash setting
    inled = Pin("LED", Pin.OUT)
    utime.sleep_ms(100)
    inled.value(1)
    utime.sleep_ms(100)
    inled.value(0)

if __name__ == '__main__':
    while True:
        LED()
        Active()
