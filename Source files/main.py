from machine import Timer, Pin, ADC, I2C
from sh1106 import SH1106_I2C
import climaA, climaC, climaB
import time
import compare_climas
import change_decision
from menu_clima import menu_clima
import final_menu
import change_humidity
import change_light
import display_initial_values
import menu_humidity_light


temp=hum=moist=light=r=g=b=result=0

#Init I2C communication
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)

#Init OLED display
oled = SH1106_I2C(i2c)

#Obtained initial values
t2,h2,l2,m2 = display_initial_values.display_initial_values()  


#Choose the adecuate clima for the plant
temp,hum,moist,light,r,g,b = menu_clima()
oled.fill_rect(0, 0, 128, 64,0)
time.sleep(3)

#Compare initial and adecuate climas
compare_climas.comparison(temp,hum,light,moist,t2,h2,l2,m2)

time.sleep(2)

#User decides to change parameters or not
result = change_decision.change_parameters(hum)

#Change parameters
if result == 1:
    #Change both
    hum = change_humidity.change_humidity(hum)
    light = change_light.change_light(r,g,b)
    
if result ==2:
    #Change humidity
    hum = change_humidity.change_humidity(hum)

if result ==3:
    #Change light
    light = change_light.change_light(r,g,b)

#Display final menu
final_menu.final_menu(temp,hum,moist,light)

#Initialize timer
tim = Timer(0)
tim.init(period=1,
         mode=Timer.PERIODIC,
         callback=menu_clima)

tim.deinit()
oled.fill_rect(0,0,128,64,0)



