# MotionSensor

<div align="center">
<img align="left" src="https://media.tenor.com/lJ3nu6akejIAAAAM/smoke-alarms-market.gif" />
<img align="right" src="https://media.tenor.com/lJ3nu6akejIAAAAM/smoke-alarms-market.gif" />

Welcome! I am going to build a "Motion Sensor" - Working with IOT devices.
Using Micro Python programming and the Raspberry Pi Pico W as well as PIR sensor, buzzer and RGB LED. I will building reliable and cost effcient alarm system. 

The aim of this project is to alert the user when motion is detected via a local web server as well as control the sensor functionality, everytime the motion is detected it will record this by using MicroPython to log data into a .txt file and/or cloud files. 

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

<div align="left">
<h3><b>Stage 1</b></h3>
<p>Circuit-Board:
Detect whether someone was present in the sensor detection area through the Raspberry Pi Pico W.
If a person is detected, the light will be turned on, and the buzzer will activate making a noise that will last the duration
of the PIR sensor motion detection which is set to detect motion at the value of '1', then buzzer and LED will activate simousltanously.
Once the PIR sensor has dected motion, from a green static RGB LED it will then change colour to red and the buzzer will activate. 
The buzzer is set to a frequency of '750' and reset after three seconds, unless motion is detected again.
(Upon simulating the usage of this product, the buzzer is noticablly heard from the next room over or within a quiet multi-level household.)</p>
<p>PIR sensor, also known as pyroelectric infrared sensor, is a sensor that uses infrared light for data
processing. Since the human body has a constant body temperature, generally around 37 degrees, it
emits infrared rays with a specific wavelength of about 10um. The infrared light emitted by the human
body is enhanced by the Philippine filter and then concentrated on the infrared induction source.</p>
</div>
<div align="left">
<h3><b>Stage 2</b></h3>
<p>Web Server:
Now that the projects basic programming is underway, its time to focus on making a sufficent web server for remote control access. Remote control access alarm system can be useful when;
  <ul>
  <li>Activation.</li>
  <li>Control.</li>
  <li>Disabling.</li>
  <li>Time Sensitive.</li>
  <li>Easy Customisation.</li>
</ul>
Within the project over time I apply all of these features to my project and mark them off one by one.</p>
</div>
<div align="left">
<h3><b>Stage 3</b></h3>
<p>Data Logging:
The final part of the project will consist of recording data and logging this data on the web server so that we can convert and save this into txt files.</p
</div>
<br>
