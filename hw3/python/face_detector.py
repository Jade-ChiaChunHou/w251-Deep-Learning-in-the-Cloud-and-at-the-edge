import numpy as np
import cv2 as cv
import paho.mqtt.client as paho
import pickle

LOCAL_MQTT_HOST = "mosquitto"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "face_detector_topic"

#callback function
def on_publish(client,userdata,result):
    print("data published \n")
    pass

#mqtt client
mqtt_client = paho.Client()
mqtt_client.on_publish = on_publish
mqtt_client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT)

#face detector
facealg = cv.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")

#connect to camera
cap = cv.VideoCapture(1)

while(True):

    #gray scale image
    ret, frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)

    #face detect
    faces = facealg.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:       
        gray_frame = gray[y:y+h, x:x+w]  
        rc,png = cv.imencode('.png', gray_frame)
        msg = pickle.dumps(png)
        mqtt_client.publish(LOCAL_MQTT_TOPIC, msg, qos=0, retain=False)
    
    #quit capturing
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
