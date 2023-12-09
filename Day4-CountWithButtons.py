from machine import Pin
import time

# Set up input pins
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up LED pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Create a list of our LEDs
segments = [seg1, seg2, seg3, seg4, seg5]

# Set the initial count for the index
count = -1

# Turn off all LEDs to start
seg1.value(0)
seg2.value(0)
seg3.value(0)
seg4.value(0)
seg5.value(0)

while True:
    time.sleep(0.01)
    
    if redbutton.value() == 1:
        if count == 4:
            pass
        else:
            count += 1
            segments[count].value(1)
            time.sleep(0.2)
    if greenbutton.value() == 1:
        if count == -1:
            pass
        else:
            segments[count].value(0)
            time.sleep(0.2)
            count -= 1