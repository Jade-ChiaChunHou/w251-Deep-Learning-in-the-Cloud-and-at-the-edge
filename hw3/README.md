# Homework 3

## Jetson TX2 Setup
### Forwarder
The code is in python/forwarder.py

### Image Process
The code is in python/img_processor.py

### Face Detect
The code is in python/face_detector.py

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
echo "56a981b6d7eb4560ad69753a9fc50cfd:8dba0da08eeacc1193d2c108305930bae3c33c7a8446ce76" > $HOME/.cos_creds
chmod 600 $HOME/.cos_creds

sudo mkdir -m 777 /mnt/mybucket
sudo s3fs bucketname /mnt/mybucket -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.us-east.objectstorage.softlayer.net
```
### Create the docker image
