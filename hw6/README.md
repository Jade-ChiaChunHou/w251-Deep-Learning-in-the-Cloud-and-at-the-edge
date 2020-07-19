# HW6

## Create the machine
> Create a P100a VM
```
ibmcloud sl vs create --datacenter=lon06 --hostname=p100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873822 --flavor AC1_8X60X100 --san
```

> Create a V100a VM
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1872864 --flavor AC2_8X60X100 --san
```

## SSH into the machine
> ssh into P100a VM
```
ssh -i ~/.ssh/id_rsa root@158.176.142.157
```

> ssh into V100a VM
```
ssh -i ~/.ssh/id_rsa root@158.175.83.187
```

## Run the docker image and open jupyter notebook in the machine

> P100a VM run docker image and open the jupyter notebook in the machine
```
nvidia-docker run --rm --name hw06 -p 8888:8888 -d w251/hw06:x86-64
```

> V100a VM run docker image and open the jupyter notebook in the machine
```
nvidia-docker run --rm --name hw06 -p 8888:8888 -d w251/hw06:x86-64
docker logs c2c4048fbb80f77901eb6dcd3420fe088627197c190cb1a59f2f1f1485a61e83
http://158.175.83.187:8888/?token=37fc80398de86348fe56f0a6aa8600fb1d0d52162ebec7c2
```

# HTML
> V100a VM
```
http://158.175.83.187:8888/notebooks/v2/week06/hw/V100_VM_BERT_classifying_toxicity_jade.ipynb
```
# Model Execute Time in VM
V100_VM spend 1h 55min 12s.

## Compare the run time of P100a VM and V100a VM
Please run it on a V100 VM and a P100 VM and report run times on training 1M rows on both. 

