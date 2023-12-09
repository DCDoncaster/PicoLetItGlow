# Imports
from machine import Pin
import time

# Set up input pins
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up output pins
redled = Pin(14, Pin.OUT)

# Set up counter variable
count = 0

while True:

    time.sleep(0.2)
    
    redled.value(0) # LED off until button press
    
    if redbutton.value() == 1:
        count = count -1
        redled.value(1) # LED on
        print(count)
        
    if greenbutton.value() == 1:
        count = count +1
        redled.value(1) # LED on
        print(count)
