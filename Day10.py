# Imports
from machine import Pin, ADC
from neopixel import NeoPixel
import time

# LED details
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs
ring = NeoPixel(Pin(GPIOnumber), LEDcount)

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# Make sure the strip is cleared before we start
ring.fill((0,0,0))
ring.write()
time.sleep(1)

# Divide the analogue range by the number of LEDs
LEDdivision = (65535/LEDcount)

while True:
    
    # Take a reading
    # Divide the reading by LED division
    # Round the reading
    reading = round( (potentiometer.read_u16()) / LEDdivision )
    ring.fill((255,0,0))
    ring.write()
    ring[reading-1] = (0,0,255)
    
#     # Set which LEDs should be ON
#     for ledon in range (reading):
#         ring[ledon] = (0,0,255)
#     
#     # Set which LEDs should be OFF
#     for ledoff in range ((reading),LEDcount,1):
#         ring[ledoff] = (0,0,0)
    
    # Write the data
    ring.write()
    time.sleep(0.1)
