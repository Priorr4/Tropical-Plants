from machine import I2C
from machine import Pin
import dht12
import network
import my_wifi
import urequests
import time

# API settings
API_KEY = "O4RP1YMLE48JR1PW"

def send_to_thingspeak(hum, light):
    API_URL = "https://api.thingspeak.com/update"

    # GET request
    url = f"{API_URL}?api_key={API_KEY}&field1={hum}&field2={light}"
    response = urequests.get(url)

    print(f"Entry # sent to ThingSpeak: {response.text}")
    response.close()


# Create Station interface
wifi = network.WLAN(network.STA_IF)
print("Start using Wi-Fi. Press `Ctrl+C` to stop")