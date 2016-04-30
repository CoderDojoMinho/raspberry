import RPi.GPIO as GPIO
import time

MOTION = 27
LED = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(MOTION, GPIO.IN)

while True:
       if GPIO.input(MOTION):
           led_output = GPIO.HIGH
       else:
           led_output = GPIO.LOW
       GPIO.output(LED, led_output)
       time.sleep(0.2)
