# Print when button switch has been pressed

import RPi.GPIO as GPIO
import time

BUTTON = 18 # Change GPIO pin here

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(BUTTON)

    if input_state == False:
        print("BUTTON PRESSED")

    time.sleep(0.2)

