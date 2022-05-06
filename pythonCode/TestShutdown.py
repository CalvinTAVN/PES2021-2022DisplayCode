# !/bin/python
# Simple script for shutting down the Raspberry Pi at the press of a button.
# by Inderpreet Singh


import RPi.GPIO as GPIO

import time

import os

# Use the Broadcom SOC Pin numbers

# Setup the pin with internal pullups enabled and pin in reading mode.

GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Our function on what to do when the button is pressed

def Shutdown(channel):
    print("Shutting Down")

    time.sleep(5)

    os.system("sudo shutdown -h now")
