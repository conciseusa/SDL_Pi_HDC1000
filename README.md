Pure Python Raspberry Pi Driver for the TI HDC1000/HDC1080 Temperature and Humidity Sensor
<BR>
Forked from switchdoclabs/SDL_Pi_HDC1000 and updated to run on Python 3.11
<BR>
Used to test the [DIN Rail Mount for Raspberry Pi Zero with GPIO](https://www.tindie.com/products/conciseusa/din-rail-mount-for-raspberry-pi-zero-with-gpio/) Board
<BR>

July 6, 2024: Forked repo, Updated to run on Python 3.11, Added fahrenheit display, Added gpio-test.py

June 26, 2017:  Fixed Accuracy Problem

March 9, 2017:  Added Serial Number, Manufacturer ID and Device ID

Initial Release:   January 2017, Version 1.0<BR>

HDC1000/HDC1080 is on default I2C address value of 0x40

Default resolution is 14 bit tempeature and 14 bit humidity<BR>
Heater is default off

To test on Raspberry Pi:

1) sudo raspi-config Interfacing Options -> I2C -> Enable

2) cd to dir to put code, `git clone https://github.com/conciseusa/SDL_Pi_HDC1000.git`

3) cd in to checkout, user@raspberrypi:~/git/SDL_Pi_HDC1000 $ `python testHDC1000.py`

4) to test LEDs, buttons, RXD port, `python gpio-test.py`
