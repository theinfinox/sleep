#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

Vibrate = 27

GPIO.setmode(GPIO.BCM)       # Numbers pins by physical location
GPIO.setup(Vibrate, GPIO.OUT)   # Set pin mode as output
GPIO.output(Vibrate, GPIO.LOW)  # Set pin to low(0V)

p = GPIO.PWM(Vibrate, 1000)     # set Frequece to 0.7KHz
p.start(0)                     # Start PWM output, Duty Cycle = 0

def Vibrate_Pin():

        try:
                while True:
                        for dc in range(0, 101, 5):   # Increase duty cycle: 0~100
                                p.ChangeDutyCycle(dc)     # Change duty cycle
                                time.sleep(0.05)
                        time.sleep(1)
                        for dc in range(100, -1, -5): # Decrease duty cycle: 100~0
                                p.ChangeDutyCycle(dc)
                                time.sleep(0.05)
                        time.sleep(1)
                        
        except KeyboardInterrupt:
                p.stop()
                GPIO.output(Vibrate, GPIO.LOW)    # turn off Vibrate
                GPIO.cleanup()

if __name__=="__main__":
        print("Vibration started. Press Ctrl+C to stop.")
        Vibrate_Pin()
        
