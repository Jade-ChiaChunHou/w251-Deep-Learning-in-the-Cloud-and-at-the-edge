# HW6

## Create the machine
> Create a p100a
```
ibmcloud sl vs create --datacenter=lon06 --hostname=p100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1872864 --flavor AC1_8X60X100 --san
```

> Create a v100a
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1872864 --flavor AC2_8X60X100 --san
```

## SSH into the machine
> ssh into p100a
```
ssh -i ~/.ssh/id_rsa root@158.176.142.157
```

> ssh into v100a
```
ssh -i ~/.ssh/id_rsa root@158.175.83.187
```

## Run the docker image and open jupyter notebook in the machine

> p100a run docker image v100a and open the jupyter notebook in the machine
```
nvidia-docker run --rm --name hw06 -p 8888:8888 -d w251/hw06:x86-64
```

> v100a run docker image v100a and open the jupyter notebook in the machine
```
nvidia-docker run --rm --name hw06 -p 8888:8888 -d w251/hw06:x86-64
docker logs c2c4048fbb80f77901eb6dcd3420fe088627197c190cb1a59f2f1f1485a61e83
http://158.175.83.187:8888/?token=37fc80398de86348fe56f0a6aa8600fb1d0d52162ebec7c2
```

