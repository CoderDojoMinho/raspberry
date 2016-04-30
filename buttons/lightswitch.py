import RPi.GPIO as GPIO
import time

BUTTON = 18
LIGHT = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LIGHT, GPIO.OUT)

light_toggle = GPIO.LOW
while True:
    input_state = GPIO.input(BUTTON)
    if input_state == False:
        if light_toggle == GPIO.HIGH:
            light_toggle = GPIO.LOW
        else:
           light_toggle = GPIO.HIGH
        GPIO.output(LIGHT, light_toggle)

    time.sleep(0.2)

