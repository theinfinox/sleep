import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

file_path = 'temperature_data.txt'

# Create or open the text file for writing
with open(file_path, 'w') as file:
    try:
        while True:
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                data_line = f"Temp={temperature:0.1f}C Humidity={humidity:0.1f}%"
                print(data_line)

                # Write the data to the file
                file.write(data_line + '\n')
            else:
                print("Sensor failure. Check wiring.")

            time.sleep(2)
