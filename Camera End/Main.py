import machine
import time
import network
import dht
from umqtt.simple import MQTTClient

def set_pin(*num):
    list_num = []
    for item in num:
        pin_id = machine.Pin(item, machine.Pin.IN, machine.Pin.PULL_UP)
        list_num.append(pin_id)
    return list_num


def read_value(list_knob):
    list_value = []
    for item in range(len(list_knob)):
        list_value.append(list_knob[item].value())
    return list_value


def set_result(import_list):

    export_value = 0

    if import_list == [1, 1, 1, 1]:
        export_value = 0
    elif import_list == [0, 1, 1, 1]:
        export_value = 1
    elif import_list == [1, 0, 1, 1]:
        export_value = 2
    elif import_list == [0, 0, 1, 1]:
        export_value = 3
    elif import_list == [1, 1, 0, 1]:
        export_value = 4
    elif import_list == [0, 1, 0, 1]:
        export_value = 5
    elif import_list == [1, 0, 0, 1]:
        export_value = 6
    elif import_list == [0, 0, 0, 1]:
        export_value = 7
    elif import_list == [1, 1, 1, 0]:
        export_value = 8
    elif import_list == [0, 1, 1, 0]:
        export_value = 9

    return export_value


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


def light_detect(pin_id):
    adc1 = machine.ADC(machine.Pin(pin_id))
    adc1.atten(machine.ADC.ATTN_11DB)
    return adc1


def light_convert(num):
    if num < 1500:
        result_value = 0
    elif num < 2000:
        result_value = 1
    elif num < 2500:
        result_value = 2
    elif num < 3000:
        result_value = 3
    elif num < 3500:
        result_value = 4
    elif num < 4000:
        result_value = 5
    else:
        result_value = 6

    return result_value


def hum_detect():
    global temp
    global hum
    global temp_f
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0


internet_connect()
#
# connect ESP to Adafruit IO using MQTT
#
myMqttClient = "itdoesnotmatter"  # replace with your own client name
adafruitUsername = "fqhang"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "f8c8109354ca4d83b7a702d9101b2fc4"  # can be found by clicking on "VIEW AIO KEYS" when viewing an Adafruit IO Feed
adafruitFeed1 = adafruitUsername + "/feeds/KnobValue1" # replace "test" with your feed name
adafruitFeed2 = adafruitUsername + "/feeds/KnobValue2" # replace "test" with your feed name
adafruitFeed3 = adafruitUsername + "/feeds/PhotoSensor" # replace "test" with your feed name
adafruitFeed4 = adafruitUsername + "/feeds/Temperature" # replace "test" with your feed name
adafruitFeed5 = adafruitUsername + "/feeds/Humidity" # replace "test" with your feed name
adafruitFeed6 = adafruitUsername + "/feeds/Switch"
adafruitIoUrl = "io.adafruit.com"
c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)


button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
photo_int = light_detect(34)

knob_green = set_pin(26, 25, 4, 14)
knob_white = set_pin(27, 33, 15, 32)

sensor = dht.DHT22(machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP))

list_value1 = read_value(knob_white)
knob_value3 = set_result(list_value1)

list_value2 = read_value(knob_green)
knob_value4 = set_result(list_value2)

c.connect()

while True:

    list_value1 = read_value(knob_white)
    knob_value1 = set_result(list_value1)

    list_value2 = read_value(knob_green)
    knob_value2 = set_result(list_value2)

    print(knob_value1)
    print(knob_value2)

    knob1_difference = knob_value1 - knob_value3
    knob2_difference = knob_value2 - knob_value4

    if knob1_difference != 0:
        print("difference" + str(knob_value1))
        c.publish(adafruitFeed6, str(knob_value1) + str(knob_value2))
        list_value1 = read_value(knob_white)
        knob_value3 = set_result(list_value1)

    if knob2_difference != 0:
        print("difference" + str(knob_value2))
        c.publish(adafruitFeed6, str(knob_value1) + str(knob_value2))
        list_value2 = read_value(knob_green)
        knob_value4 = set_result(list_value2)

    time.sleep(0.5)

    if not button.value():

        list_value1 = read_value(knob_white)
        knob_value1 = set_result(list_value1)

        list_value2 = read_value(knob_green)
        knob_value2 = set_result(list_value2)

        photo_value = light_convert(photo_int.read())

        hum_detect()

        c.publish(adafruitFeed1, str(knob_value1))
        c.publish(adafruitFeed2, str(knob_value2))
        c.publish(adafruitFeed3, str(photo_value))
        c.publish(adafruitFeed4, str(temp_f))
        c.publish(adafruitFeed5, str(hum))

        print(list_value1)
        print(knob_value1)
        print(list_value2)
        print(knob_value2)
        print(photo_int.read())
        print(photo_value)
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)
        time.sleep(0.5)

# 1.upload the data to the cloud
# 2.control two switches at the same time
# 3.connect to the esp32 to detect the sensors and print the variables
# 4.write classes
