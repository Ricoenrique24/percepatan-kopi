import RPi.GPIO as GPIO
import time

# Konfigurasi pin GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

# Fungsi untuk mengontrol relay
def control_relay(pin, state):
    GPIO.output(pin, state)

# Contoh penggunaan
while True:
    control_relay(16, GPIO.HIGH)  # Nyalakan relay
    time.sleep(1)
    control_relay(16, GPIO.LOW)  # Matikan relay
    time.sleep(1)