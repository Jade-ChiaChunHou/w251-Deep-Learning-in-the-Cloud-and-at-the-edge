FROM python:3.7-alpine3.11
RUN apk update && apk upgrade
RUN apk --no-cache add mosquitto mosquitto-clients
RUN pip3 install paho-mqtt
EXPOSE 1883
