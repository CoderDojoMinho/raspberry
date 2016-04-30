import RPi.GPIO as GPIO
import time

MOTION = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION, GPIO.IN)

while True:
       if GPIO.input(MOTION):
           print("Motion detected!")
       time.sleep(0.2)
