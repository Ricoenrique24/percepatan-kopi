import RPi.GPIO as GPIO
import time

# Konfigurasi pin GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.output)

# Contoh penggunaan
while True:
    GPIO.output(17, GPIO.HIGH)  # Nyalakan relay
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)  # Matikan relay
    time.sleep(1)