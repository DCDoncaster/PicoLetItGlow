# Imports
from machine import Pin
import time

# Pin Setup Variables
green = Pin(25, Pin.OUT)
red = Pin(14, Pin.OUT)
count = 0

# Loop Program
while count < 10: #Loop forever
    print(count)
    red.value(1) #LED on
    green.value(1)
    time.sleep(0.2) #Wait a short time
    
    red.value(0) #LED off
    green.value(0)
    time.sleep(0.2) #wait a short time
    count += 1
    
 