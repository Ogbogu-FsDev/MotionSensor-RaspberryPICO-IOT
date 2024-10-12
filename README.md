# MotionSensor

Welcome! I am going to build a "Motion Sensor" - Working with IOT devices.
Using Micro Python programming and the Raspberry Pi Pico W as well as PIR sensor, buzzer and RGB LED. I will building reliable and cost effcient alarm system. 

The aim of this project is to alert the user when motion is detected via a local web server, everytime the motion is detected I am going to use MicroPython and any other eternal sources for logging that data in either a txt or cloud files.

Hardware:
  - 1x Raspberry Pi PICO W
  - 1x SunFounder Breadboard Power Bank (Power Supply Module)
  - 1x Medium Breadboard
  - 1x PIR Sensor (Motion Sensor)
  - 1x RGB LED
  - 1x Buzzer
  - 10x Dupont Line
  - 10x Male-Male short line
  

Basic:
Once the PIR sensor has dected motion, from a green static RGB LED it will then change colour to red and the buzzer will activate. The buzzer is set to a frequency of '750' and reset after three seconds, unless motion is detected again. (Upon simulating the usage of this product, the buzzer is noticablly heard from the next room over or within a quiet multi-level household.)

Web Server:
Now that the projects basic programming is underway, its time to focus on making a sufficent web server for remote control access. Remote control access alarm system can be useful when;
  - Activation.
  - Control.
  - Disabling.
  - Time Sensitive.
  - Easy Customisation.
Within the project over time I apply all of these features to my project and mark them off one by one.

Data Logging:
The final part of the project will consist of recording data and logging this data on the web server so that we can convert and save this into txt files.
