# MotionSensor

<div align="center">
<img align="left" src="https://media.tenor.com/lJ3nu6akejIAAAAM/smoke-alarms-market.gif" />
<img align="right" src="https://media.tenor.com/lJ3nu6akejIAAAAM/smoke-alarms-market.gif" />

Welcome! I am going to build a "Motion Sensor" - Working with IOT devices.
Using Micro Python programming with a Raspberry Pi Pico W, PIR sensor, buzzer and RGB LED. With these eltronic componets I am striding to build a reliable and efficient remote access alarm system.

The aim of this project is to activate an alarm system, manually, automatically or remotely. The project is able to make an alarm noise to ward off trespassers, when activated. Once the alarm has been tripped it then alerts the users when motion is detected via a local web server as well as control the sensor functionality, everytime motion is detected it will record Date and Time of the detection by logging data into a .txt file and/or cloud files.

** Raspberry Pi Pico W (Current Project) **
---------------------------
Storage info
---------------------------
Storage space on this drive or filesystem:

    total space: 848.0 kB
    used space: 36.0 kB
    free space: 812.0 kB

---------------------------
---------------------------
</div>
<br>
<b>Hardware Requirements:</b>
<ul>
<img align="right" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjEnWJpbTcO-sJU5no65Hrhvb4nkBJPfLrqPnocyUqgjDbI73hE74UMNqy5RkIO4IWcttuTFEcr4PioLZhNf9JE50XHHg3YCdjNhM94x7bXTJdWXWuA8R8c9hs3XvNW5az2hNb2ptnDw/s1600/pilogo.gif" />
  <li>1x Raspberry Pi PICO W</li>
  <li>1x SunFounder Breadboard Power Bank (Power Supply Module)</li>
  <li>1x Medium Breadboard</li>
  <li>1x PIR Sensor (Motion Sensor)</li>
  <li>1x RGB LED</li>
  <li>1x Buzzer</li>
  <li>10x Dupont Line</li>
  <li>10x Male-Male short line</li>
</ul>
<br>

<img align="left" src="https://www.diyprojectslab.com/wp-content/uploads/2022/11/Raspberry-pi-pico-W-Led-blinking.gif" />
<div align="left">
<h3><b>Stage 1 - Circuit-Board:</b></h3>
<p>PIR sensor, also known as pyro-electric infrared sensor, is a sensor that uses infrared light for data
processing. Since the human body has a constant body temperature, generally around 37 degrees, it
emits infrared rays with a specific wavelength of about 10um. The infrared light emitted by the human
body is enhanced by the Philippine filter and then concentrated on the infrared induction source.</p>

<p>Detect whether someone was present in the sensor detection area through the Raspberry Pi Pico W.
If a person is detected, the light will be turned on, and the buzzer will activate making a noise that will last the duration
of the PIR sensor motion detection which is set to detect motion at the value of '1', then buzzer and LED will activate simultaneously.
Once the PIR sensor has detected motion, from a green static RGB LED it will then change colour to red and the buzzer will activate.
The buzzer is set to a frequency of '750' and reset after three seconds, unless motion is detected again.
(Upon simulating the usage of this product, the buzzer is noticeably heard from the next room over or within a quiet multi-level household.)</p>
</div>

<img width=500 align="right" src="https://how2electronics.com/wp-content/uploads/2022/11/Pi-Pico-W-Webserver-MicroPython.jpg" />
<div align="left">
<h3><b>Stage 2 - Web Server:</b></h3>
<p>Now that the project's main programming and circuit board are completed
  Web server hardware is connected to the internet and allows data to be exchanged with other connected devices.
  Remote control access needs to be established for the alarm system to be useful when;
  <ul>
    <li>Activation.</li>
    <li>Control.</li>
    <li>Disabling.</li>
    <li>Time Sensitive.</li>
    <li>Easy Customisation.</li>
  </ul>
</p>
</div>

<img width=250  height=250 align="left" src="https://i.pinimg.com/originals/fb/68/41/fb6841b5b9701782a9dd24bd6702da5a.gif"/>
<img width=250  height=250 align="right" src="https://i.pinimg.com/originals/a2/b4/ae/a2b4ae4ebabcd10ff10a1581366f6df2.gif"/>
<div align="center">
<h3><b> Stage 3 - Data Logging - .txt file:</b></h3>
<p> The Next stage will cover data logging to a (txt) file,
  part of the project will consist of recording data and logging this data in a txt file.
  The web server will also come in handy to view data remotely.
</p>
</div>
<div align="center">
<h3><b> Stage 4 - Data Logging - cloud computing:</b></h3>
<p> cloud computing is the delivery of computing services—including servers,
  storage, databases, networking, software and more.</p>
</div>
<br>
