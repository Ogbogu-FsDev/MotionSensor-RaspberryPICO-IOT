# Motion Sensor

<div align="center">
Welcome! I am going to build a "Motion Sensor" - Working with micro-controllers and IOT devices.
Using Micro Python programming with a Raspberry Pi Pico W, PIR sensor, buzzer and RGB LED. With these electronic components I am striding to build a reliable and efficient remote access alarm system.

The aim of this project is to activate an alarm system, manually, automatically or remotely. The project is able to make an alarm noise to ward off trespassers, when activated. Once the alarm has been tripped it then alerts the users when motion is detected via a local web server as well as control the sensor's functionality within the web server, every time motion is detected it will record the Date and Time of the detection by logging data into a .txt file and/or cloud file.

This project is ideal for monitoring pet in/out goings. From birds nest, cat flaps, hamster wheel. A various range of ideas to be hosted by this motion sensing project.

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
<p>
<b>Port connection:</b> 

Raspberry PICO W | RGB LED | BUZZER | PIR Sensor |
--- | --- | --- | --- |
GP0 |   |   | S |
GP2 | R |   |   |
GP3 | G |   |   |
GP4 | B |   |   |
GP14 |   | Buz |   |
3V3 |   |   | + |
GND | - | - | - |
</p>

<p>
<b>Current Project Issues:</b> 
whilst working on this project I have encountered a few issue, here I will state the current issues with my project and update my read me on my resolve.
- <b>WIFI connection</b> - make sure to turn the PICO on and off for a fresh restart, this makes it easier to connect to the WIFI with out any errors occurring.
- <b>buzzer</b> - receives electricity causing the buzzer to be triggered when the alarm system is in occurrence with the 'else' statement and 'buzzer.deinit()' is declared but proves not to work.
</p>
<img align="left" src="https://www.diyprojectslab.com/wp-content/uploads/2022/11/Raspberry-pi-pico-W-Led-blinking.gif" />
<div align="left">
<h3><b>Stage 1 - Circuit-Board:</b></h3>
<p>PIR sensor, also known as pyro-electric infrared sensor, is a sensor that uses infrared light for data
processing. Since the human body has a constant body temperature, generally around 37 degrees, it
emits infrared rays with a specific wavelength of about 10um. The infrared light emitted by the human
body is enhanced by the Philippine filter and then concentrated on the infrared induction source.</p>

<p>Detecting whether someone was present in the sensor detection area through the Raspberry Pi Pico W.
If a person is detected, the light will be turned on, and in accordance the buzzer will activate making a noise that will last the duration
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

<div align="left">
<h3><b> Stage 3 - Data Logging - .txt file:</b></h3>
<p> The Next stage will cover data logging to a (txt) file,
  part of the project will consist of recording data and logging this data in a txt file.
  The web server will also come in handy to view data remotely.
</p>
</div>
<br>
