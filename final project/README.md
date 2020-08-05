# Final Project
Github repo link: https://github.com/ksjeyabarani/v2/tree/w251_prj/project 

## 1. Create a V100_VM in ibm cloud
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100 --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873850 --flavor AC2_16X120X100 --san

ssh -i ~/.ssh/id_rsa root@158.175.102.149
```

## 2. Code setup
```
cd && git clone https://github.com/Jade-ChiaChunHou/w251-Deep-Learning-in-the-Cloud-and-at-the-edge
cd /w251-Deep-Learning-in-the-Cloud-and-at-the-edge/final project
```

## 3. python environment setup
```
apt install python3-pip
pip3 install virtualenv
source venv/bin/activate
pip install -r requirements.txt
```

## 4. Download Kaggle 

Go to Kaggle 'Account' Tab of the user profile and select 'Create API Token'. This will trigger the download of kaggle.json and put it in the /root/.kaggle directory.

```
cd && kaggle competitions download -c global-wheat-detection
apt install unzip
cd && unzip global-wheat-detection.zip
```

```
cp -avr train /root/global-wheat-detection/
cp -avr test /root/global-wheat-detection/
cp train.csv /root/global-wheat-detection

cd /root/w251-Deep-Learning-in-the-Cloud-and-at-the-edge/final project/code
python pytorch-fasterrcnn-train.py

```



