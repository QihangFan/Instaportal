import machine
import time
import network
import ssd1306
from umqtt.simple import MQTTClient

# OLED Display

def initDisplay():
    print("initDisplay called.")
    oled.init_display()
    oled.fill(0)
    oled.text("Hello" , 0, 0)
    oled.text("Welcome to" , 0, 10)
    oled.text("Instaportal" , 0, 20)
    oled.show()

def internet_connect():
    # connect the ESP to local wifi network
    #
    yourWifiSSID = "ACCD"
    yourWifiPassword = "tink1930"
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
      sta_if.active(True)
      sta_if.connect(yourWifiSSID, yourWifiPassword)
      while not sta_if.isconnected():
        pass

    print("connected to WiFi")


def sub_cb(topic, msg):
    global value
    value = list(str(msg,'utf-8'))
    print(value)

def obj_mode(int):
    if int == '0':
        oled.text("LandScape Mode", 0, 0)
    elif int == '1':
        oled.text("Portrait Mode", 0, 0)
    elif int == '2':
        oled.text("Animal Mode", 0, 0)
    elif int == '3':
        oled.text("Plant Mode", 0, 0)
    elif int == '4':
        oled.text("Sky Mode", 0, 0)
    elif int == '5':
        oled.text("Architecture Mode", 0, 0)
    elif int == '6':
        oled.text("Furniture Mode", 0, 0)
    elif int == '7':
        oled.text("Prairie Mode", 0, 0)
    elif int == '8':
        oled.text("Space Mode", 0, 0)
    elif int == '9':
        oled.text("Illusion Mode", 0, 0)

def mood_mode(int):
    if int == '0':
        oled.text("Happy Mode", 0, 10)
    elif int == '1':
        oled.text("Cry Mode", 0, 10)
    elif int == '2':
        oled.text("Blue Mode", 0, 10)
    elif int == '3':
        oled.text("Angry Mode", 0, 10)
    elif int == '4':
        oled.text("Casual Mode", 0, 10)
    elif int == '5':
        oled.text("Excited Mode", 0, 10)
    elif int == '6':
        oled.text("Crazy Mode", 0, 10)
    elif int == '7':
        oled.text("Desired Mode", 0, 10)
    elif int == '8':
        oled.text("Relax Mode", 0, 10)
    elif int == '9':
        oled.text("Scare Mode", 0, 10)


i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23), freq = 100000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
initDisplay()

internet_connect()
value = []
#
# connect ESP to Adafruit IO using MQTT
#
myMqttClient = "esp32"  # replace with your own client name
adafruitUsername = "fqhang"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "f8c8109354ca4d83b7a702d9101b2fc4"  # can be found by clicking on "VIEW AIO KEYS" when viewing an Adafruit IO Feed
adafruitFeed1 = adafruitUsername + "/feeds/Switch" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"
c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)

c.connect()
while True:
    time.sleep(0.5)
    c.set_callback(sub_cb)
    c.subscribe(bytes(adafruitFeed1,'utf-8'))
    c.check_msg()

    if len(value) == 2:
        oled.fill(0)
        obj_mode(value[0])
        mood_mode(value[1])
        oled.text("@instaportal", 0, 20)
        oled.show()



