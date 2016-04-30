# Light up a LED while the switch is down

import RPi.GPIO as GPIO
import time

BUTTON = 18
LIGHT = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LIGHT, GPIO.OUT)

while True:
    input_state = GPIO.input(BUTTON)
    if input_state == False:
        GPIO.output(LIGHT, GPIO.HIGH)
    else:
        GPIO.output(LIGHT, GPIO.LOW)

    time.sleep(0.2)

