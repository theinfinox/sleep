import RPi.GPIO as GPIO
import time

# GPIO pin numbers
button_pin = 23
vibrator_pin = 27

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(vibrator_pin, GPIO.OUT)
vibrator_on = False

def toggle_vibrator(channel):
    global vibrator_on
    vibrator_on = not vibrator_on
    if vibrator_on:
        GPIO.output(vibrator_pin, GPIO.HIGH)
        print("Vibrator ON")
    else:
        GPIO.output(vibrator_pin, GPIO.LOW)
        print("Vibrator OFF")

# Add an event detection for the button press
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=toggle_vibrator, bouncetime=200)

try:
    while True:
        # Do other tasks or just keep the program running
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
