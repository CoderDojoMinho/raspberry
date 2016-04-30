# Continuously scrolls a message in a LCD

import os, sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), "lib/adafruit/Adafruit_CharLCD"))

from Adafruit_CharLCD import Adafruit_CharLCD as CharLCD

DURATION = 30
START_POSITION = 14 # Have the text scroll left. Adjust for LCD size
current_time = lambda: int(round(time.time()))
start_time = current_time()

msg = 'CODERDOJO\nMINHO'
split = msg.split('\n')

position = START_POSITION
max_len = max(len(split[0]), len(split[1])) 

lcd = CharLCD(pin_rs=2, pin_e=4, pins_db=[3, 14, 25, 24])
lcd.clear()
lcd.begin(16,2)
lcd.setCursor(14,0)
lcd.message(split[0])
lcd.setCursor(14,1)
lcd.message(split[1])


while current_time() < start_time + DURATION:
  lcd.DisplayLeft()
  position = (position + 1) % max_len
  time.sleep(.3)

for x in range(position, START_POSITION + max_len):
  lcd.DisplayLeft()
  time.sleep(.3)

lcd.clear()

