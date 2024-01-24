
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 1

# Define the mapping function
def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Create or open the text file for writing
with open('decibel_values.txt', 'w') as file:
    try:
        while True:
            sensorValue = adc.read_adc(0, gain=GAIN)

            # Map the sensor value to the decibel range
            decibelValue = map_value(sensorValue, 0, 32767, 35, 110)  # Adjust the input and output ranges as needed

            # Write the decibel value to the file
            file.write(f"decibelValue = {decibelValue}\n")

            print("decibelValue =", decibelValue)
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass  # Allow the program to exit gracefully when Ctrl+C is pressed

# File will be automatically closed when leaving the 'with' block

