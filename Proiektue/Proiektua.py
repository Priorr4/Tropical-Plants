from machine import I2C
from machine import Pin
from sh1106 import SH1106_I2C
import time
import dht12

SENSOR_ADDR = 0x5c

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400_000)
print(f"I2C configuration : {str(i2c)}")
# Init OLED display
oled = SH1106_I2C(i2c)
sensor = dht12.DHT12(i2c)

try:
    # Forever loop
    while True:
        temp, humidity = sensor.read_values()
        print(f"Temperature: {temp}°C Humidity: {humidity}%")
        # Add some text at (x, y)
        oled.text(f"Humidity: {humidity}",0,2)
        oled.text(f"Temperat: {temp}",0,12)
        oled.show()
        oled.fill_rect(70,1,58,22,0)
        ###print(f"{val[0]}.{val[1]} %")
        
        time.sleep(5)

except KeyboardInterrupt:
    # This part runs when Ctrl+C is pressed
    print("Program stopped. Exiting...")


