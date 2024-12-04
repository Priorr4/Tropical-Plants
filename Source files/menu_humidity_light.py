from machine import Timer, Pin, ADC, I2C
from sh1106 import SH1106_I2C
import time
import change_humidity

hor = ADC(Pin(34))
ver = ADC(Pin(35))
push = Pin(27,Pin.IN,Pin.PULL_UP)
hor.atten(ADC.ATTN_11DB)      
ver.atten(ADC.ATTN_11DB)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)
asec=0
csec=0

def humidity_light(hum):
#Choose which parameters are wanted to change
    global asec, csec, bsec
    
    oled = SH1106_I2C(i2c)
    oled.text('Choose parameter:',0, 0) 
    oled.text('Humidity:',0, 10) 
    oled.text('Light: PUSH',0, 23)
    oled.text('Humidity+Light',0, 36)
    
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
   
    pos_x, pos_y = 73, 10
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

    pos_x, pos_y = 117, 36
    for j, row in enumerate(icon):
        for i, val in enumerate(row):
            oled.pixel(i+pos_x, j+pos_y, val)
    oled.show()
    
    """Read the input from the joystick and
    show the changes that will be made.
    The user must be one second selecting its choice"""

    while asec<10 and csec<10 and push.value()==1:
        hor_value = hor.read()
        ver_value = ver.read()
        if hor_value<1000:
            asec+=1
            oled.text('Humidity+Light',0,53)
            oled.show()
        elif hor_value>3000:
            csec+=1
            oled.text('Humidity',0,53)
            oled.show()
        else:
            asec=0
            csec=0
            oled.fill_rect(0, 50, 128, 64,0)
            
    
    
    if asec>=10 and csec<10:
       #humidity and light functions
       return 1
    elif csec>=10 and asec<10:
        #humidity function
        return 2
    else:
        #light function
        return 3

tim = Timer(0)
tim.init(period=1,
         mode=Timer.PERIODIC,
         callback=humidity_light)
tim.deinit()