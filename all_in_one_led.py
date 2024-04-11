import RPi.GPIO as GPIO
import time

# Set the GPIO pins for the red, green, blue, and white LEDs
red_pin = 12
green_pin = 6
blue_pin = 16
white_pin = 13
tap_pin = 24

# Set the GPIO pins as outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(white_pin, GPIO.OUT)
GPIO.setup(tap_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set up the tap pin as input with pull-up resistor

# Function to change colors
def change_color(color):
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(blue_pin, GPIO.LOW)
    GPIO.output(white_pin, GPIO.LOW)

    if color == "red":
        GPIO.output(red_pin, GPIO.HIGH)
    elif color == "green":
        GPIO.output(green_pin, GPIO.HIGH)
    elif color == "blue":
        GPIO.output(blue_pin, GPIO.HIGH)
    elif color == "white":
        GPIO.output(white_pin, GPIO.HIGH)
    elif color == "yellow":
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.HIGH)
    elif color == "cyan":
        GPIO.output(green_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.HIGH)
    elif color == "magenta":
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.HIGH)
    elif color == "off":
        pass  # All LEDs are off

# Function for breathing effect
def breathing():
    for duty_cycle in range(0, 101, 5):
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)
    for duty_cycle in range(100, -1, -5):
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)

# Function for fade in and out effect
def fade_in_out():
    for duty_cycle in range(0, 101, 5):
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.4)
    for duty_cycle in range(100, -1, -5):
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.2)

# Define interrupt handler function
def tap_callback(channel):
    global tap_time, tap_count
    current_time = time.time()

    # Check if it's a double tap
    if current_time - tap_time < 0.5:  # 0.5 seconds between taps for a double tap
        tap_count += 1
        if tap_count == 1:
            breathing()
        elif tap_count == 2:
            fade_in_out()
            tap_count = 0  # Reset tap count after second tap
    else:
        # Reset tap count if it's a single tap
        tap_count = 0
        # Change color for single tap
        change_color("red")
        time.sleep(1)
        change_color("green")
        time.sleep(1)
        change_color("blue")
        time.sleep(1)
        change_color("white")
        time.sleep(1)
        change_color("yellow")
        time.sleep(1)
        change_color("cyan")
        time.sleep(1)
        change_color("magenta")
        time.sleep(1)
        change_color("off")

    tap_time = current_time

tap_time = time.time()  # Initialize tap time
tap_count = 0  # Initialize tap count

# Add interrupt for tap detection
GPIO.add_event_detect(tap_pin, GPIO.FALLING, callback=tap_callback, bouncetime=300)

# Setup PWM for breathing and fade in & out effects
GPIO.setup(white_pin, GPIO.OUT)
pwm = GPIO.PWM(white_pin, 100)
pwm.start(0)

try:
    while True:
        pass  # Your main program loop can continue here if needed

except KeyboardInterrupt:
    # Clean up the GPIO pins and PWM
    pwm.stop()
    GPIO.cleanup()
