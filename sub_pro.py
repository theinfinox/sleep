import subprocess
import sys

def main():
    try:
        # Start subprocesses for each component
        voice_assistant = subprocess.Popen([sys.executable, '/home/pi/Desktop/voice//main.py'])
        vibrator = subprocess.Popen([sys.executable, '/home/pi/Desktop/voice/vibrator.py'])
        led = subprocess.Popen([sys.executable, '/home/pi/Desktop/voice/led.py'])
        temp_humidity = subprocess.Popen([sys.executable, '/home/pi/Desktop/voice/temp_humidity.py'])
        sound_sensor = subprocess.Popen([sys.executable, '/home/pi/Desktop/voice/sound_sensor.py'])

        # Wait for subprocesses to finish
        voice_assistant.wait()
        vibrator.wait()
        led.wait()
        temp_humidity.wait()
        sound_sensor.wait()

    except KeyboardInterrupt:
        # Terminate all subprocesses if KeyboardInterrupt is detected
        voice_assistant.terminate()
        vibrator.terminate()
        led.terminate()
        temp_humidity.terminate()
        sound_sensor.terminate()

if __name__ == "__main__":
    main()
