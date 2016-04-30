# Light up a single LED for one second
# GPIO number given as the first argument to the script

import RPi.GPIO as GPIO
import time
from sys import argv

light = int(argv[1])

GPIO.setmode(GPIO.BCM)
GPIO.setup(light, GPIO.OUT)

GPIO.output(light, GPIO.HIGH)
time.sleep(1)
GPIO.output(light, GPIO.LOW)

GPIO.cleanup()
