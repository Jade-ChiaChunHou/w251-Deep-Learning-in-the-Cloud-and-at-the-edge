# Homework 3

## Jetson TX2 Setup


### Face Detect
The docker image is in DockerFile/face_detecor. The python code is in python/face_detector.py.
```
sudo docker build /home/nvidia/w251/hw3/dockerfile/face_detector
```
### Forwarder
The code is in python/forwarder.py

### Broker
The docker image is in DockerFile/broker.
```
sudo docker build /home/nvidia/w251/hw3/dockerfile/broker
```

### Image Process
The docker image is in DockerFile/img_processor. The code is in python/img_processor.py
```
sudo docker build /home/nvidia/w251/hw3/dockerfile/img_processor
```

## IBM Cloud Setup

### Create Cloud Storage Object (S3)
Create a Cloud Storage Object in IBM Cloud. Select the lite plan in cloud.ibm.com/resources.

### Install the IBM Cloud Storage Object on our VSI
```
sudo apt-get update
sudo apt-get install automake autotools-dev g++ git libcurl4-openssl-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
git clone https://github.com/s3fs-fuse/s3fs-fuse.git
cd s3fs-fuse
./autogen.sh
./configure
make
sudo make install
```
### Add the Cloud Storage Object Credentials
```
echo "<Access_Key_ID>:<Secret_Access_Key>" > $HOME/.cos_creds
chmod 600 $HOME/.cos_creds

sudo mkdir -m 777 /mnt/mybucket
sudo s3fs bucketname /mnt/mybucket -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.us-east.objectstorage.softlayer.net
```
### Create the docker image
