import machine, neopixel
n = 31
p = 25
r=0
g=0
b=0
np= neopixel.NeoPixel(machine.Pin(p),n)
for i in range(n):
    np[i]=(r,g,b)
np.write()