# HW6

## Create the machine
> Create a p100a
```
ibmcloud sl vs create --datacenter=lon06 --hostname=p100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1841164 --flavor AC1_8X60X100 --san
```

> ### Create a v100a
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1841164 --flavor AC2_8X60X100 --san
```

## SSH into the machine
> ## ssh into p100a
```
ssh -i ~/.ssh/id_rsa root@158.176.142.157
```

## run this in the machine
nvidia-docker run --rm --name hw06 -p 8888:8888 -d w251/hw06:x86-64
