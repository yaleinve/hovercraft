#comment

import RPi.GPIO as GPIO
import time
from gpiozero import DistanceSensor

LedPin = 3
pin_to_circuit = 17

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led

def blink():
  while True:
    GPIO.output(LedPin, GPIO.HIGH)  # led on
    time.sleep(1)
    GPIO.output(LedPin, GPIO.LOW) # led off
    time.sleep(1)

def distance():
    ultrasonic = DistanceSensor(echo=17, trigger=4)  # values are the GPIO pins
    while True:
       print(ultrasonic.distance)
       time.sleep(1)

def destroy():
  GPIO.output(LedPin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    blink()
    # distance()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()

  #Catch when script is interrupted, cleanup correctly
  try:
    # Main loop
    while True:
      print rc_time(pin_to_circuit)
  except KeyboardInterrupt:
    GPIO.output(pin_to_circuit, GPIO.LOW)   # light sensor off
    GPIO.cleanup() 

