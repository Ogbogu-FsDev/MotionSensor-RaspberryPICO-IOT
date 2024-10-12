from machine import Pin, PWM, Timer, I2C
import utime

PIR = Pin(0, Pin.IN, Pin.PULL_DOWN)   #Motion sensor 
Led_R = PWM(Pin(4))
Led_G = PWM(Pin(3))
Led_B = PWM(Pin(2))
buzzer = PWM(Pin(12, Pin.IN)) #Sound
Led_R.freq(2000)   # Set the frequency to 2KHz
Led_G.freq(2000)   
Led_B.freq(2000)
buzzer.duty_u16(1000)
    
def Alarm():
    print(PIR.value())
    if PIR.value() == 1:
        buzzer.freq(750)
        Led_R.duty_u16(65535)
        Led_G.duty_u16(0)
        Led_B.duty_u16(0)
        utime.sleep(3)
    else:
        buzzer.deinit()
        Led_R.duty_u16(0)
        Led_G.duty_u16(65535)
        Led_B.duty_u16(0)

def StopAlarm():
    if PIR.value() == 1:
        buzzer.deinit()
        Led_R.duty_u16(0)
        Led_G.duty_u16(0)
        Led_B.duty_u16(65535)
        utime.sleep(2)
        Led_R.duty_u16(0)
        Led_G.duty_u16(0)
        Led_B.duty_u16(65535)
        utime.sleep(3)
    else:
        buzzer.deinit()
        Led_R.duty_u16(0)
        Led_G.duty_u16(65535)
        Led_B.duty_u16(0)
