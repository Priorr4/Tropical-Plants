from machine import Timer, Pin, ADC, I2C
from sh1106 import SH1106_I2C
import math,time
import final_menu

hor = ADC(Pin(34))
ver = ADC(Pin(35))
hor.atten(ADC.ATTN_11DB)      
ver.atten(ADC.ATTN_11DB)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)
oled = SH1106_I2C(i2c)
relay = Pin(5, mode=Pin.OUT)
push = Pin(27,Pin.IN,Pin.PULL_UP)


def change_humidity(hum_to_change):
#Set the new values of humidity
    
    oled.text('Change humidity:',0, 0) 
    oled.text('Increase',0, 10) 
    oled.text('Decrease',0, 23)
    oled.text('Exit = Push',0, 36)


#Customized characters (arrows)
    icon = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
   
    pos_x, pos_y = 70, 23
    for j, row in enumerate(icon):
        for i, val in enumerate(row):
            oled.pixel(i+pos_x, j+pos_y, val)



    icon = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    pos_x, pos_y = 70, 10
    for j, row in enumerate(icon):
        for i, val in enumerate(row):
            oled.pixel(i+pos_x, j+pos_y, val)
    oled.show()
    
#Select humidity value
    while True:
        hor_value = hor.read()
        ver_value = ver.read()
        
        if hor_value<1000:
            relay.on()
            hum_to_change = float(hum_to_change) + 0.1 
            oled.text(f'New hum={round(hum_to_change,2)}%',0,50)
            oled.show()
            oled.fill_rect(0, 50, 128, 64,0)
        elif hor_value>3000:
            relay.on()
            hum_to_change = float(hum_to_change) - 0.1
            oled.text(f'New hum={round(hum_to_change,2)}%',0,50)
            oled.show()
            oled.fill_rect(0, 50, 128, 64,0)
        else:
            oled.text(f'New hum={round(hum_to_change,2)}%',0,50)
            oled.fill_rect(0, 50, 128, 64,0)
            relay.off()
        if push.value()==0:
            break
    hum1 = round(hum_to_change,2)
    return hum1
        

