import paho.mqtt.client as mqtt
import cv2 as cv
import time
import pickle
from datetime import datetime

#local info
LOCAL_MQTT_HOST = "remote-broker"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "img_processor_topic"
PATH = "/mnt/mybucket/"

#local callback function
def on_connect_local(client, userdata, flags, rc):
        print("Connect image processor and broker: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client,userdata, msg):
  try:
    print("\n Received processed image")

    img = pickle.loads(msg.payload)
    png = cv.imdecode(img, 0)
    ts = str(datetime.timestamp(datetime.now())).replace('.','-', 1)
    filename = PATH + 'face-' + ts + '.png'
    print("Saving", filename)
    cv.imwrite(filename, png)

  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
