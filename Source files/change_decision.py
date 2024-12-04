from machine import Timer, Pin, ADC, I2C
from sh1106 import SH1106_I2C
import menu_humidity_light

hor = ADC(Pin(34))
ver = ADC(Pin(35))
hor.atten(ADC.ATTN_11DB)      
ver.atten(ADC.ATTN_11DB)

#Init I2C communication
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)

asec=0
csec=0
result=0 
def change_parameters(hum):
#User decides to change parameters or not
    global asec, csec, bsec
    
    oled = SH1106_I2C(i2c)
    oled.text('Change parameters?',0, 0) 
    oled.text('Yes',0, 10) 
    oled.text('No',0, 23)

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
   
    pos_x, pos_y = 27, 10
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

    pos_x, pos_y = 27, 23
    for j, row in enumerate(icon):
        for i, val in enumerate(row):
            oled.pixel(i+pos_x, j+pos_y, val)
    oled.show()
    
    
    while asec<10 and csec<10:
        hor_value = hor.read()
        ver_value = ver.read()
        print(f"asec: {asec}\t csec: {csec}\t hor:{hor_value}")
        if hor_value<1000:
            asec+=1
            oled.text('No change',0,50)
            oled.show()
        elif hor_value>3000:
            csec+=1
            oled.text('Change',0,50)
            oled.show()
        else:
            asec=0
            csec=0
            oled.fill_rect(0, 50, 128, 64,0)
    #No change        
    if asec>=10 and csec<10:
        pass
    
    #Change    
    elif csec>=10 and asec<10:
        result = menu_humidity_light.humidity_light(hum)
        return result
    return
    



tim = Timer(0)
tim.init(period=1,
         mode=Timer.PERIODIC,
         callback=change_parameters)
tim.deinit()