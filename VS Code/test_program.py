import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)     # Ignore warning
GPIO.setmode(GPIO.BOARD)    # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set

# Loop function:
while True:
    GPIO.output(8, GPIO.HIGH)
    io_state = GPIO.input(8)
    print("IO State:", io_state)
    sleep(1)
    GPIO.output(8, GPIO.LOW)
    io_state = GPIO.input(8)
    print("IO State:", io_state)
    sleep(1)