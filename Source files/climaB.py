from machine import I2C
from machine import Pin
from sh1106 import SH1106_I2C
import math
import neopixel

n=31
np = neopixel.NeoPixel(Pin(25), n)
r=75
g=110
b=128
def climaB():
#Display parameters of clima B
    
    #Init I2C communication
    i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400_000)
    # Init OLED display
    oled = SH1106_I2C(i2c)
    
    moisture= 4*math.log10(75)
    rounded_moisture = round(moisture, 1)
    oled.text("Clima B:",0,2)
    oled.text("Temperat: 29 C",0,12)
    oled.text("Humidity: 75%",0,22)
    oled.text(f"Moisture: {rounded_moisture}%",0,32)
    oled.text("Light: 45%",0,42)
    for i in range(n):
        np[i] = (r,g,b)
        np.write()
    oled.show()
    
    return 29,75,rounded_moisture,45,r,g,b