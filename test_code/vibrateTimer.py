import RPi.GPIO as GPIO
import time

# Define the GPIO pin number for the Vibrator
VIBRATOR_PIN = 27

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Setup the Vibrator pin as an output
GPIO.setup(VIBRATOR_PIN, GPIO.OUT)

# Function to create the Vibrator effect
def Vibrator():
    try:
        while True:
            # MOTOR ON (High Speed)
            GPIO.output(VIBRATOR_PIN, GPIO.HIGH)
            time.sleep(0.1)
            
            # MOTOR OFF (Low Speed)
            GPIO.output(VIBRATOR_PIN, GPIO.LOW)
            time.sleep(0.1)
            
            
    except KeyboardInterrupt:
        # Turn off the MOTOR and clean up on Ctrl+C
        GPIO.output(VIBRATOR_PIN, GPIO.LOW)
        GPIO.cleanup()

if __name__ == "__main__":
    print("Vibration started. Press Ctrl+C to stop.")
    Vibrator()
