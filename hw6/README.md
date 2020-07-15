# HW6

## Create a p100a
```
ibmcloud sl vs create --datacenter=lon06 --hostname=p100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1841164 --flavor AC1_8X60X100 --san
```

## Create a v100a
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1841164 --flavor AC2_8X60X100 --san
```
