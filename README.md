# MotionSensor

<div align="center">
<img align="left" src="https://media.tenor.com/lJ3nu6akejIAAAAM/smoke-alarms-market.gif" />
<img align="right" src="https://media.tenor.com/lJ3nu6akejIAAAAM/smoke-alarms-market.gif" />

Welcome! I am going to build a "Motion Sensor" - Working with IOT devices.
Using Micro Python programming and the Raspberry Pi Pico W as well as PIR sensor, buzzer and RGB LED. I will building reliable and cost effcient alarm system. 

The aim of this project is to alert the user when motion is detected via a local web server, everytime the motion is detected I am going to use MicroPython and any other eternal sources for logging that data in either a txt or cloud files.
</div>
<br>

<b>Hardware:</b>
  - 1x Raspberry Pi PICO W
  - 1x SunFounder Breadboard Power Bank (Power Supply Module)
  - 1x Medium Breadboard
  - 1x PIR Sensor (Motion Sensor)
  - 1x RGB LED
  - 1x Buzzer
  - 10x Dupont Line
  - 10x Male-Male short line
<br>

<div align="left">
<h3><b>Stage 1</b></h3>
Circuit-Board:
Detect whether someone was present in the sensor detection area through the Raspberry Pi Pico W. If
a person is detected, the light will be turned on, and the buzzer will activate making a noise that will last the duration
of the PIR sensor motion detection which is set to detect motion at the value of '1', then buzzer and LED will activate simousltanously.
Once the PIR sensor has dected motion, from a green static RGB LED it will then change colour to red and the buzzer will activate. The buzzer is set to a frequency of '750' and reset after three seconds, unless motion is detected again. (Upon simulating the usage of this product, the buzzer is noticablly heard from the next room over or within a quiet multi-level household.)
PIR sensor, also known as pyroelectric infrared sensor, is a sensor that uses infrared light for data
processing. Since the human body has a constant body temperature, generally around 37 degrees, it
emits infrared rays with a specific wavelength of about 10um. The infrared light emitted by the human
body is enhanced by the Philippine filter and then concentrated on the infrared induction source.
</div>
<br>

<div align="left">
<h3><b>Stage 2</b></h3>
Web Server:
Now that the projects basic programming is underway, its time to focus on making a sufficent web server for remote control access. Remote control access alarm system can be useful when;
  - Activation.
  - Control.
  - Disabling.
  - Time Sensitive.
  - Easy Customisation.
Within the project over time I apply all of these features to my project and mark them off one by one.
</div>
<br>

<div align="left">
<h3><b>Stage 3</b></h3>
Data Logging:
The final part of the project will consist of recording data and logging this data on the web server so that we can convert and save this into txt files.
</div>
<br>
