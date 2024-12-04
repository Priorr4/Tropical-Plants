from machine import I2C
from machine import Pin
from machine import ADC
from sh1106 import SH1106_I2C
import time

push = Pin(27,Pin.IN,Pin.PULL_UP)

#Init I2C communication
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400_000)
#Init OLED display
oled = SH1106_I2C(i2c)
    
def final_menu(temp,humidity,moisture,light):
#Display final clima parameters
    
        oled.text("Selected clima:",0,2)
        oled.text(f"Temperat: {temp}C",0,12)
        oled.text(f"Humidity: {humidity}%",0,22)
        oled.text(f"Moisture: {moisture}%",0,32)
        oled.text(f"Light: {light}%",0,42)

        oled.show()
        oled.fill_rect(0,0,128,64,0)
        
        time.sleep(5)
        
        oled.text('Plant growing!',15,32)
        oled.show()
    
        
