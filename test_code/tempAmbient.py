import Adafruit_DHT
import time
import keyboard

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

# Create or open the text file for writing
with open('temperature_data.txt', 'w') as file:
    try:
        while True:
            if keyboard.is_pressed('Ctrl') and keyboard.is_pressed('x'):  # Check if Ctrl + x are pressed
                break  # Exit the loop and stop the program
                
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                data_line = "Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)
                print(data_line)
                
                # Write the data to the file
                file.write(data_line + '\n')
            else:
                print("Sensor failure. Check wiring.")
            time.sleep(2)
    except KeyboardInterrupt:
        pass  # Allow the program to exit gracefully when Ctrl+C is pressed

# File will be automatically closed when leaving the 'with' block
