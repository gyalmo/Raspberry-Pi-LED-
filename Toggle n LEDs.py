#WAP to toggle n LEDs
#n=3

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup (18,GPIO.OUT)
GPIO.setup (17,GPIO.OUT)
GPIO.setup (16,GPIO.OUT)
for i in range (0,10):
   GPIO.output(18,GPIO.HIGH)
   GPIO.output(17,GPIO.LOW)
   GPIO.output(16,GPIO.HIGH)
   time.sleep(3)
   GPIO.output(18,GPIO.LOW)
   GPIO.output(17,GPIO.HIGH)
   GPIO.output(16,GPIO.LOW)
   time.sleep(3)


