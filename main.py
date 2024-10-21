import network
import socket
import time
import machine

from sequence import *
from data import *
from machine import Pin

# Identify Local Network
intled = machine.Pin("LED", machine.Pin.OUT)
  
ssid = s_id
password = p_word
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# HTML - Web Page
html = """<!DOCTYPE html>
    <html>
        <head>
            <title>Motion Sensor</title>
            <style>
            body {
                background-color: black;
                text-align: center;
            }
            h1, h2 {
                color: lightgreen;
                text-decoration: underline;
                font-weight: bold;
            }
            .alarm, .led {
                color: lightgreen;
                font-size: 30px;
            }
            </style>
        </head>
        <body>
            <h1>Pico W: Motion Sensor</h1>
            <h2>System Call</h2>
            <br>
            
            <div class="led">
            <h3>Onboard LED</h3>
            <a href='/LEDon'><button>LED On</button></a>
            <a href='/LEDoff'><button>LED Off</button></a>
            </div>
            
            <div class="alarm">
            <h3>Alarm Settings</h3>
            <a href='/ALARMon'><button>Alarm On</button></a>
            <a href='/ALARMoff'><button>Alarm Off</button></a>
            </div>
            
        </body>
    </html>
"""
 
# Waiting to connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
 
# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

stateis = ""
 
# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)

        request = cl.recv(1024)
        print(request)
        request = str(request)
    
        led_on = request.find('/LEDon')
        led_off = request.find('/LEDoff')
        
        alarm_on = request.find('/ALARMon')
        alarm_off = request.find('/ALARMoff')
        
        # Onboard LED Controls
        if led_on == 6:
            print(" LED is on")
            while True:
                LEDon()
        elif led_off == 6:
            print(" LED is off")
            while True:
                LEDoff()
                
        # Alarm System Controls
        elif alarm_on == 6:
            print(" Alarm is on")
            while True:
                Active()
        elif alarm_off == 6:
            print(" Alarm is off")
            while True:
                InActive()
                
        response = html + stateis
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
 
    except OSError as e:
        cl.close()
        print('connection closed')
