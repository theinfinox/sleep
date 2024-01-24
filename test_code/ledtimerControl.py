import RPi.GPIO as GPIO
import time

# Define the GPIO pin number for the LED
LED_PIN = 18

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Setup the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to create the heartbeat effect
def heartbeat_led():
    try:
        while True:
            # LED ON (bright)
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.5)
            
            # LED OFF (dim)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.5)
            
            # LED ON (bright)
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.5)
            
            # LED OFF (longer delay to simulate heartbeat pause)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        # Turn off the LED and clean up on Ctrl+C
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()

if __name__ == "__main__":
    print("Heartbeat LED started. Press Ctrl+C to stop.")
    heartbeat_led()
