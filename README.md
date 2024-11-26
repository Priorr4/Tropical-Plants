# Tropical-Plants
  Project descrption:
  
  [Display](https://wokwi.com/projects/413911746413303809)

  [Matlab](https://wokwi.com/projects/415642410000224257)
## Team members
  Joritz Legarda-Ereño Aranguren
  
  June Lizaso Aguirre
  
  Laura Prior Urbizu
  
  Joseba Sagarzazu Oteiza
## Hardware descrption
This are all the hardaware components used in this project:
- Joystick
- RGB lights
- MicroPython OLED display
- BreadBoard
- ESP32 WROOM 32D
- Light dependance resistance (LDR)
- Relay

We have made a research on each hardware component that we have implemented in this project.

### Joystick:

The fundamental concept behind the analog joystick involves two linked potentiometers that convey data on **vertical (Y-axis) and horizontal (X-axis) motion**. Furthermore, the joystick is equipped with a select button that **works like a switch.**

Joystick consist on 5 pins. `VCC` and `GND` are connected to the corresponding pins in the breadboard. 

There are other two pins, in this case **analog pins**, that control X and Y axis movement, `Vrx` and `Vry` respectively. In the case of X axis, this pin is connected to `PIN34` (A2) of the microcontroller, whereas Y axis is connected to `PIN35` (A3). 

The last pin is a **digital** one and works like a switch when de joystick is pressed. This one is connected to **`NOSE QUE PIN ESSSSSSSSS`** ().

The analog values are shown on the picture below:

![AXIS](https://github.com/user-attachments/assets/92c7a02c-9c00-4f7e-a628-b52b0fd4d918) 

In this case analog values are computed between **0 and 4095**.

![Joystick](https://www.electronicwings.com/storage/PlatformSection/TopicContent/123/description/Joystick2.jpg)

### RGB light:
**Used Model:** `RGB LED strip Neopixel WS2812B`

A LED strip is a flexible circuit board that contains a series of small Light Emitting Diodes (LEDs) mounted along its length.

This model has three pins.`VCC` and `GND` are connected to the corresponding pins in the breadboard. The third PIN is called DINPIN, this digital pin i connected to `PIN


![RGB light](https://cdn.myshoptet.com/usr/www.laskakit.cz/user/shop/big/8416-2_led-pasek-neopixel-ws2812b-144led-m-ip30-1m-cerny.jpg?628f60c2)

### MicroPython OLED display:
![Display](https://devreyakan.com/wp-content/uploads/2022/07/image-9.png.webp)

### Breadboard:
A breadboard is a flat, perforated board that allows components and wires to be **easily inserted and connected** for building and testing electronic circuits.

A breadboard has **rows and columns of holes**, with the holes in the same row connected electrically. The rows are typically connected horizontally, while the columns are for positioning components. By inserting components into these holes, electrical connections are made between the holes in the same row, allowing components to interact without soldering.

![BreadBoard](https://electropeak.com/pub/media/catalog/product/cache/bc5042bf121eb5dcbd431cdc7ec1fd5b/c/a/cab-01-002-1-bread-board-8-5-8-5cm.jpg)

### ESP32 WROOM 32D:
![ESP32](https://ce8dc832c.cloudimg.io/v7/_cdn_/BE/B6/90/00/0/617451_1.jpg?width=640&height=480&wat=1&wat_url=_tme-wrk_%2Ftme_new.png&wat_scale=100p&ci_sign=ecbc082e1968d44612ae5635e6defb9c957a3da9)

### Light dependance resistance (LDR):
![LDR](https://techdelivers.com/image/cache/catalog/Sensor%20Modules/Optical/ldr-light-dependent-resistor-600x315w.jpg)

### Relay:
![Relay](https://www.robotechbd.com/wp-content/uploads/2021/04/relay-5v.jpg)


## Software description:


## Instructions and photos:

## References and tools:

[proiektuen aurreapena](https://wokwi.com/projects/415155736853765121)

[ioritz_analog_irakurri](https://randomnerdtutorials.com/esp32-esp8266-analog-readings-micropython/)

[rgb funtzionamendua](https://esp32io.com/tutorials/esp32-ws2812b-led-strip)

[Configuration RelayMode - Python](https://www.upesy.com/blogs/tutorials/esp32-relay-module-with-micropython-code?srsltid=AfmBOop7Rz4NttnxwDSwEVrj7ANNDrtH8H_BS9dAkLuB1RZGA2uLwb5F)



