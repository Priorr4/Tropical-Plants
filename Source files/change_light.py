from machine import Pin, ADC, I2C
import time 
import neopixel
from sh1106 import SH1106_I2C

ldr = ADC(Pin(15))
ldr.atten(ADC.ATTN_11DB)    

hor = ADC(Pin(34))
ver = ADC(Pin(35))
hor.atten(ADC.ATTN_11DB)      
ver.atten(ADC.ATTN_11DB)

#Init I2C communication
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)

# Init OLED display
oled = SH1106_I2C(i2c)

n=31
push = Pin(27,Pin.IN,Pin.PULL_UP)

np = neopixel.NeoPixel(Pin(25), n)
def change_light(r, g, b):
#Change the intensity of light into a desired one
    r_prop=r/g
    b_prop=b/g

    oled.text('Change light:',0, 0) 
    oled.text('Increase',0, 10) 
    oled.text('Decrease',0, 23)
    oled.text('Exit = Push',0, 36)

    icon = [
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0]]
   
    pos_x, pos_y = 70, 23
    for j, row in enumerate(icon):
        for i, val in enumerate(row):
            oled.pixel(i+pos_x, j+pos_y, val)



    icon = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0]]

    pos_x, pos_y = 70, 10
    for j, row in enumerate(icon):
        for i, val in enumerate(row):
            oled.pixel(i+pos_x, j+pos_y, val)
    oled.show()
    time.sleep(1)
    
    while True:
        hor_value = hor.read()
        ver_value = ver.read()
        ldr_value = ldr.read()
        light = ldr_value*100//4095
        time.sleep(0.01)
    
        """Increase RGB values proportionally
        depending on theposition of the joystick
        without surpassing the maximum values."""
        
        if ver_value>3000 and 0<=round(r)<255 and 0<=round(g)<255 and 0<=round(b)<255:
            r+=r_prop
            g+=1
            b+=b_prop
            
        elif ver_value<1000 and 0<round(r)<=255 and 0<round(g)<=255 and 0<round(b)<=255:
            r+=-r_prop
            g+=-1
            b+=-b_prop

        oled.text(f'Intensity={light}%',0,50)
        oled.show()
        oled.fill_rect(0, 50, 128, 64,0)

        """Writing the acquired
        values in the RGB stip"""
        for i in range(n):
            np[i] = (round(r), round(g), round(b))
            np.write()

        if push.value()==0:
            break
    return light