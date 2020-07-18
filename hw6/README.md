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
ssh -i ~/.ssh/id_rsa root@158.176.142.149
```

> ssh into v100a
```
ssh -i ~/.ssh/id_rsa root@158.175.83.185
docker logs f2fb621bab38830b938c157301b2adf68b07ae1c6ee674fb02abeda356909d4b
http://158.175.83.185:8888/?token=b8759449802091c811a369391535b50236f753ae5c47e43
```

## Run the docker image in the machine
```
nvidia-docker run --rm --name hw06 -p 8888:8888 -d w251/hw06:x86-64
containerid: b534fd07345a315fb0210c8d1b8f7569f4e77ab61916318fe68edcb34484a831

docker logs b534fd07345a315fb0210c8d1b8f7569f4e77ab61916318fe68edcb34484a831
docker logs 9d75e776ddd606dad167570c86274cc8bba5a89b52a7ea514e357fdaffedc6cf
http://158.176.142.149:8888/?token=260fb8c4210625ab754af11a63f5c18d0aa60cd4c185c875

http://127.0.0.1:8888/?token=724e4e43f72c3ef3c924da27b9c76ba66bb15d56ca3d37f3
http://127.0.0.1:8888/?token=25b3f7d94586fa413297306ac2e1f156f54b1aefd41888dc
http://158.176.142.157:8888/?token=724e4e43f72c3ef3c924da27b9c76ba66bb15d56ca3d37f3
http://158.176.142.157:8888/?token=25b3f7d94586fa413297306ac2e1f156f54b1aefd41888dc
```
