#WAP to release LED

import RPi.GPIO as GPIO

import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)
GPIO.output(17,GPIO.LOW)
GPIO.output(16,GPIO.HIGH)

