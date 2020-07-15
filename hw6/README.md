# HW6

## Create the machine
> Create a p100a
```
ibmcloud sl vs create --datacenter=lon06 --hostname=p100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1841164 --flavor AC1_8X60X100 --san
```

> Create a v100a
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1841164 --flavor AC2_8X60X100 --san
```

## SSH into the machine
> ssh into p100a
```
ssh -i ~/.ssh/id_rsa root@158.176.142.157
```

> ssh into v100a
```
```

## Run the docker image in the machine
```
nvidia-docker run --rm --name hw06 -p 8888:8888 -d w251/hw06:x86-64
containerid: b534fd07345a315fb0210c8d1b8f7569f4e77ab61916318fe68edcb34484a831

docker logs b534fd07345a315fb0210c8d1b8f7569f4e77ab61916318fe68edcb34484a831
http://127.0.0.1:8888/?token=724e4e43f72c3ef3c924da27b9c76ba66bb15d56ca3d37f3
http://158.176.142.157:8888/?token=724e4e43f72c3ef3c924da27b9c76ba66bb15d56ca3d37f3

```
