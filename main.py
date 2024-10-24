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
                    .container {
                        display: grid;
                        grid-template-columns: 16rem 1fr 16rem;
                        grid-template-rows: auto 1fr auto;
                        grid-template-areas:
                            "header header header"
                            "nav content sidebar"
                            "footer footer footer";
                        min-height: 100vh;
                    }
                    header {
                        grid-area: header;
                        padding: 2rem;
                        background-color: burlywood;
                    }
                    .title {
                        font-family: cursive;
                        color: maroon;
                        text-decoration: underline;
                        font-weight: bold;
                        text-align: center;
                        margin-top: auto;
                    }
                    nav {
                        grid-area: nav;
                        padding: 2rem;
                        background-color: bisque;
                    }
                    main {
                        grid-area: content;
                        padding: 2rem;
                        background-color: rgb(236, 202, 139);
                    }
                    .settings {
                        font-family: cursive;
                        color: black;
                        text-align: left;
                    }
                    aside {
                        grid-area: sidebar;
                        padding: 2rem;
                        background-color: bisque;
                    }
                    footer {
                        grid-area: footer;
                        padding: 2rem;
                        background-color: burlywood;
                    }
                    @media (max-width:1024px) {
                        .container {
                            display: grid;
                            grid-template-columns: 1fr;
                            grid-template-rows: auto minmax(5rem, auto) 1fr  minmax(5rem, auto) auto;
                            grid-template-areas:
                            "header"
                            "nav"
                            "content"
                            "sidebar"
                            "footer";
                            min-height: 100vh;
                        }
                    }
                    .button {
                        background-color: #ecba30;
                        border: none;
                        color: white;
                        padding: 16px 40px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        cursor: pointer;
                        display: inline-block;
                        text-align: center;
                    }
                    .button1 {
                        background-color: #a04b06;
                    }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <header>
                            <h1 class="title">Raspberry Pi PICO W - Motion Sensor</h1>
                        </header>
                        <nav>Navbar</nav>
                        <main>
                            <h2 class="title">Frame</h2>
                            <div>
                                <p>
                                    <i class="fas fa-lightbulb fa-3x" style="color:#ecba30;"></i>
                                    <a href=\"1\"><button class="button">XXXX</button></a>
                                    <i class="far fa-lightbulb fa-3x" style="color:#a04b06;"></i>
                                    <a href=\"2\"><button class="button button1">XXXX</button></a>
                                </p>
                            </div>
                        </main>
                        <aside>
                            <h2 class="title">System</h2>
                                <h4 class="settings">O. LED</h4>
                                    <a href='/LEDon'><button>LED On</button></a>
                                    <a href='/LEDoff'><button>LED Off</button></a>
                                <h4 class="settings">Activate Alarm</h4>
                                    <a href='/ALARMon'><button>Alarm On</button></a>
                                    <a href='/ALARMoff'><button>Alarm Off</button></a>
                                <h4 class="settings">Silence Buzzer</h4>
                                    <a href='/mute'><button>Mute</button></a>
                                    <a href='/unmute'><button>Unmute</button></a>
                        </aside>
                        <footer>Footer</footer>
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
            while True:
                LEDon()
                if led_off == 6:
                    break
        # Alarm System Controls
        if alarm_on == 6:
            while True:
                Active()
                if alarm_off == 6:
                    break
                
        response = html + stateis
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
 
    except OSError as e:
        cl.close()
        print('connection closed')
