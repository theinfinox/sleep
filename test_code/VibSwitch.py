import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the button and vibrator
button_pin = 23  # You can change this to the actual GPIO pin you are using for the button
vibrator_pin = 27  # You can change this to the actual GPIO pin you are using for the vibrator

# Set the button pin as an input with a pull-down resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set the vibrator pin as an output
GPIO.setup(vibrator_pin, GPIO.OUT)

# Define a function to be executed when the button is pressed
def button_callback(channel):
    print("Button was pressed!")
    
    # Turn on the vibrator for 1 second
    GPIO.output(vibrator_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(vibrator_pin, GPIO.LOW)

# Add an event handler for the button press event
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    print("Press the button to activate the vibrator (Ctrl+C to exit)")
    while True:
        # Your main program logic can be here
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Clean up GPIO settings
GPIO.cleanup()
