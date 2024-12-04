from machine import Pin, I2C
from sh1106 import SH1106_I2C
import time

#Init I2C communication
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
relay = Pin(5, Pin.OUT)
oled_width = 128
oled_height = 64
oled = SH1106_I2C(i2c)

#t1,h1,l1,m1 values of clima A, B or C
#t2,h2,l2,m2 initial clima values
t1=h1=l1=m1=t2=h2=l2=m2=0

def comparison(t1,h1,l1,m1,t2,h2,l2,m2):
    """Display a menu which shows the differencies between
    measured values and selected clima values."""

    oled.fill_rect(0,0,128,64,0)
    oled.text('Desired',0, 0) 
    oled.text(f'Tem:{t1}C',0, 10) 
    oled.text(f'Hum:{h1}%',0, 23)
    oled.text(f'Lig:{l1}%',0, 36)
    oled.text(f'Soi:{m1}%',0, 49)
    oled.vline(66, 0, 64, 1)
    oled.text('Current',68, 0)
    oled.text(f'{t2}C',70, 10) 
    oled.text(f'{h2}%',70, 23)
    oled.text(f'{l2}%',70, 36)
    oled.text(f'{m2}%',70, 49)
    oled.show()
    time.sleep(1)

#Update values
    if t1 > t2:
        while t1 > t2:
            t2 += 0.1
            oled.fill_rect(70,10,30,10,0)
            oled.text(f'{round(t2,1)}C',70,10)
            oled.show()
    if t2 > t1:
        while t2 > t1:
            t2 -= 0.1
            oled.fill_rect(70,10,30,10,0)
            oled.text(f'{round(t2,1)}C',70,10)
            oled.show()
            
    if h1 > h2:
        while h1 > h2:
            relay.on()
            h2 += 0.1
            oled.fill_rect(70,23,30,10,0)
            oled.text(f'{round(h2,1)}%',70,23)
            oled.show()
        relay.off()    
    if h2 > h1:
        while h2 > h1:
            relay.on()
            h2 -= 0.1
            oled.fill_rect(70,23,30,10,0)
            oled.text(f'{round(h2,1)}%',70,23)
            oled.show()
        relay.off()
        
    if l1 > l2:
        while l1 > l2:
            l2 += 0.1
            oled.fill_rect(70,36,30,10,0)
            oled.text(f'{round(l2,1)}%',70,36)
            oled.show()
    if l2 > l1:
        while l2 > l1:
            l2 -= 0.1
            oled.fill_rect(70,36,30,10,0)
            oled.text(f'{round(l2,1)}%',70,36)
            oled.show()
    
    if m1 > m2:
        while m1 > m2:
            m2 += 0.1
            oled.fill_rect(70,49,30,10,0)
            oled.text(f'{round(m2,1)}%',70,49)
            oled.show()
    if m2 > m1:
        while m2 > m1:
            m2 -= 0.1
            oled.fill_rect(70,49,30,10,0)
            oled.text(f'{round(m2,1)}%',70,49)
            oled.show()
