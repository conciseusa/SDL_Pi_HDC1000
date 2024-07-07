
import RPi.GPIO as GPIO
import datetime
import time
import sys
import serial

if sys.version_info.major != 3:
    sys.exit('Python3 required')

# simple script to test reading/writing GPIO pins connected to a
# https://www.tindie.com/products/conciseusa/din-rail-mount-for-raspberry-pi-zero-with-gpio/
# https://www.raspberrypi.com/documentation/computers/raspberry-pi.html
# to run
# change cd to dir gpio-test.py resides
# python3 gpio-test.py
# to run and log output
# python3 gpio-test.py >> gpio-test.log
# auto run at startup, put in crontab, adjust dir to your setup
# sleep 60 - wait for GPIO to be ready when cron calls script
# @reboot sleep 60 && python /home/username/git/gpio-test.py
# to read data from the serial port, make it is correctly configured -> sudo raspi-config
# Interfacing Options, Serial, login shell over serial - No, Serial Port Hardware - Yes, reboot to take effect


print(datetime.datetime.now(), ' start gpio-test.py')

# port /dev/serial0 for the serial device. RPiOS links this to the correct hardware during boot
ser = serial.Serial(port='/dev/serial0', baudrate = 9600, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

sweep_delay = .2
read_delay = 1

# GPIO.setwarnings(False) # to disable warnings
GPIO.setmode(GPIO.BCM)

#GPIO.cleanup() # switches all GPIO you used back to being inputs

def gpio_out(D1, D2, D3, D4, setup=False):
    if setup:
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)

    GPIO.output(4, D1) # GPIO.LOW, GPIO.HIGH
    GPIO.output(27, D2)
    GPIO.output(22, D3)
    GPIO.output(23, D4)


def gpio_read(setup=False):
    if setup:
        GPIO.setup(4, GPIO.IN)
        GPIO.setup(27, GPIO.IN)
        GPIO.setup(22, GPIO.IN)
        GPIO.setup(23, GPIO.IN)

    # read buttons
    state4 = GPIO.input(4)
    state27 = GPIO.input(27)
    state22 = GPIO.input(22)
    state23 = GPIO.input(23)

    sdata = ser.read(10) # not trying to do anything useful other then see if the serial port works
    # button state 1 = not pushed, 0 = pushed (active low)
    print(datetime.datetime.now(), ' S1: ', state4, ' S2: ', state27, ' S3: ', state22, ' S4: ', state23, ' sdata: ', sdata)


while True:

    # test the LEDs
    sweep_count = 20
    while sweep_count:
        gpio_out(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, True)
        time.sleep(sweep_delay)
        gpio_out(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH)
        time.sleep(sweep_delay)
        gpio_out(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)
        time.sleep(sweep_delay)
        gpio_out(GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
        time.sleep(sweep_delay)
        gpio_out(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)
        time.sleep(sweep_delay)
        gpio_out(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH)
        time.sleep(sweep_delay)
        sweep_count -= 1

    # continue # to only run LED sweep

    gpio_out(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW) # flash all on to signal leaving sweep mode
    time.sleep(.1)

    gpio_read(True)
    read_count = 20
    while read_count:
        gpio_read()
        time.sleep(read_delay) # the read rate may be slower depending on if the serial read in gpio_read is timing out
        read_count -= 1

    gpio_out(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, True) # flash all on to signal entering sweep mode
    time.sleep(.1)
    gpio_out(GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)
    time.sleep(2) # wait a moment to let user stop pushing buttons
