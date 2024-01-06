# Imports
from machine import Pin, ADC
from neopixel import NeoPixel
import time
import random

# Define the strip pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2), 12)

slider = ADC(Pin(28))

speed = 0

GRBvalue = 0
analoguereading = 0

# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()
time.sleep(1)
        
while True:
    analoguereading = slider.read_u16()
    GRBvalue = round(analoguereading * (255 / 65535))
    speed = slider.read_u16() / 65000
    # Select a random LED
    randomled = random.randint(0,11)
    
    # Create random RGB values
    r = random.randint(0,GRBvalue)
    g = random.randint(0,GRBvalue)
    b = random.randint(0,GRBvalue)
    
    # Light the random LED in a random colour
    ring[randomled] = (r,g,b)
    ring.write()
        
    # Show the light for this long
    time.sleep(speed)
        
    #Clear the ring at the end of each loop
    ring.fill((0,0,0))
    ring.write()
