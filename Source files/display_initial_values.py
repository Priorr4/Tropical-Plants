from machine import I2C
from machine import Pin
from machine import ADC
from sh1106 import SH1106_I2C
import time, dht12, math, neopixel

ldr = ADC(Pin(15))
ldr.atten(ADC.ATTN_11DB)       
moisture = ADC(Pin(39))
moisture.atten(ADC.ATTN_11DB)

def display_initial_values():
    """Measure and show the initial
    values in the display"""
    
    #Init I2C communication
    i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400_000)
    # Init OLED display
    oled = SH1106_I2C(i2c)
    sensor = dht12.DHT12(i2c)

    temp, humidity = sensor.read_values()
    ldr_value = ldr.read()
    moisture_value = moisture.read()
    light = ldr_value*100//4095
    moisture1 = moisture_value*100/4095
    rounded_moisture = round(moisture1, 1)
              
    oled.text(f"Temperat: {temp}",0,2)
    oled.text(f"Humidity: {humidity}%",0,12)
    oled.text(f"Moisture: {rounded_moisture}%",0,22)
    oled.text(f"Light: {light}%",0,32)
    
    oled.show()
    oled.fill_rect(70,1,58,22,0)
        
    time.sleep(5)

    return temp,humidity,light,rounded_moisture
