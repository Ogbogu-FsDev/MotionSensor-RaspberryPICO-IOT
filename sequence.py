from machine import Pin, PWM, Timer, I2C
import utime

# PIR (Motion) Sensor
PIR = Pin(0, Pin.IN, Pin.PULL_DOWN)

# RGB LED
Led_R = PWM(Pin(4))
Led_G = PWM(Pin(3))
Led_B = PWM(Pin(2))

# Buzzer 
buzzer = PWM(Pin(12, Pin.IN)) #Sound

# Set the frequency to 2KHz
Led_R.freq(2000)  
Led_G.freq(2000)   
Led_B.freq(2000)
buzzer.duty_u16(1000)

# Activating the alarm system    
def Active():
    if PIR.value() == 1:
        print(PIR.value())
        buzzer.freq(750)
        Led_R.duty_u16(65535)
        Led_G.duty_u16(0)
        Led_B.duty_u16(0)
        utime.sleep(3)
    else:
        print(PIR.value())
        buzzer.deinit()
        Led_R.duty_u16(0)
        Led_G.duty_u16(65535)
        Led_B.duty_u16(0)
        
def InActive():
    if PIR.value() == 0:
        print("Alarm Deactivated")
        Led_R.duty_u16(0)
        Led_G.duty_u16(0)
        Led_B.duty_u16(65535)
        utime.sleep(300)
