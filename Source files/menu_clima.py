from machine import Timer, Pin, ADC, I2C
from sh1106 import SH1106_I2C
import climaA, climaC, climaB
import time
import compare_climas
import change_decision

hor = ADC(Pin(34))
ver = ADC(Pin(35))
push = Pin(27,Pin.IN,Pin.PULL_UP)
hor.atten(ADC.ATTN_11DB)      
ver.atten(ADC.ATTN_11DB)

#Init I2C communication
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)
asec=csec=0
temp=hum=moist=light=0

#Init OLED display
oled = SH1106_I2C(i2c)

def menu_clima():
    """A menu to decide which clima
    is going to be implemented."""

    global asec, csec, bsec
    
    
    oled.text('Choose climate',0, 0) 
    oled.text('A climate:',0, 10) 
    oled.text('B climate: PUSH ',0, 23)
    oled.text('C climate:',0, 36)

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
    
    pos_x, pos_y = 100, 10
    for j, row in enumerate(icon):
        for i, val in enumerate(row):
            oled.pixel(i+pos_x, j+pos_y, val)


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
   
    

    pos_x, pos_y = 100, 36
    for j, row in enumerate(icon):
        for i, val in enumerate(row):
            oled.pixel(i+pos_x, j+pos_y, val)
    oled.show()
    
    
    while asec<10 and csec<10 and push.value()==1:
        hor_value = hor.read()
        ver_value = ver.read()
        if hor_value<1000:
            asec+=1
            oled.text('Choosing A',0,50)  #Clima A
            oled.show()
        elif hor_value>3000:
            csec+=1
            oled.text('Choosing C',0,50)  #Clima C
            oled.show()
        else:
            asec=0
            csec=0
            oled.fill_rect(0, 50, 128, 64,0)
            
    if asec>=10 and csec<10:
       temp,hum, moist, light,r,g,b = climaA.climaA()  #Clima A values
    elif csec>=10 and asec<10:
        temp,hum, moist, light,r,g,b = climaC.climaC()  #Clima C values
    else:
        temp,hum, moist, light,r,g,b =climaB.climaB()  #Clima B values
    
    return temp,hum,moist,light,r,g,b

tim = Timer(0)
tim.init(period=1,
         mode=Timer.PERIODIC,
         callback=menu_clima)
tim.deinit()

