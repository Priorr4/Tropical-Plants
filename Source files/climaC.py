from machine import I2C
from machine import Pin
from sh1106 import SH1106_I2C
import math
import neopixel

n=31
np = neopixel.NeoPixel(Pin(25), n)
r=g=128
b=90
def climaC():
#Display parameters of clima C
    
    #Init I2C communication
    i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400_000)
    #Init OLED display
    oled = SH1106_I2C(i2c)
    
    moisture= 4*math.log10(80)
    rounded_moisture = round(moisture, 1)
    oled.text("Clima C:",0,2)
    oled.text("Temperat: 25 C",0,12)
    oled.text("Humidity: 80%",0,22)
    oled.text(f"Moisture: {rounded_moisture}%",0,32)
    oled.text("Light: 70%",0,42)
    for i in range(n):
        np[i] = (r,g,b)
        np.write()
    oled.show()    
    
    return 25,70,rounded_moisture,70,r,g,b