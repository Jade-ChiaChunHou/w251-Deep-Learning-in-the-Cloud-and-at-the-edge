# HW9

## Create the machine

"upgrade" them by adding a second 2 TB SAN drive to each VM, then format the 2TB disk and mount it to /data on each VM as described here under the "prepare the second disk" section. 

> Create a P100a VM
```
ibmcloud sl vs create --datacenter=lon06 --hostname=p100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873850 --flavor AC1_16X120X100 --san
```

> Create a P100b VM
```
ibmcloud sl vs create --datacenter=lon06 --hostname=p100b --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873850 --flavor AC1_16X120X100 --san
```

> Create a V100a VM
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873850 --flavor AC2_16X120X100 --san
```

> Create a V100b VM
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100b --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873850 --flavor AC2_16X120X100 --san
```
