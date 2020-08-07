# HW9

### Create the machine
Upgrade the VM by adding a second 2 TB SAN drive to each of them, then format the 2TB disk and mount it to /data on each VM as described here under the "prepare the second disk" section. 

### P100a VM
> Create a P100a VM
```
ibmcloud sl vs create --datacenter=lon06 --hostname=p100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873850 --flavor AC1_16X120X100 --san
```
> ssh into P100a VM
```
ssh -i ~/.ssh/id_rsa root@158.176.142.157
```

### P100b VM
> Create a P100b VM
```
ibmcloud sl vs create --datacenter=lon06 --hostname=p100b --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873850 --flavor AC1_16X120X100 --san
```
> ssh into P100b VM
```
ssh -i ~/.ssh/id_rsa root@158.176.142.150
```
mpirun -n 2 -H 10.72.250.235,10.72.250.215 --allow-run-as-root hostname
```
nohup mpirun --allow-run-as-root -n 4 -H 10.72.250.235:2,10.72.250.215:2 -bind-to none -map-by slot --mca btl_tcp_if_include eth0 -x NCCL_SOCKET_IFNAME=eth0 -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH python run.py --config_file=/data/transformer-base.py --use_horovod=True --mode=train_eval &
```

### V100a VM
> Create a V100a VM
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100a --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873850 --flavor AC2_16X120X100 --san
```
> ssh into V100a VM
```
ssh -i ~/.ssh/id_rsa root@158.175.102.156
```

### V100b VM
> Create a V100b VM
```
ibmcloud sl vs create --datacenter=lon04 --hostname=v100b --domain=dima.com --image=2263543 --billing=hourly  --network 1000 --key=1873850 --flavor AC2_16X120X100 --san
```
> ssh into V100b VM
```
ssh -i ~/.ssh/id_rsa root@158.175.102.146
ssh-keygen -R 158.175.102.146
```

### Docker setup
```
docker build -t openseq2seq -f Dockerfile .
docker run --runtime=nvidia -d --name openseq2seq --net=host -e SSH_PORT=4444 -v /data:/data -p 6006:6006 openseq2seq
docker exec -ti openseq2seq bash
docker container start
```

### Check the connection
```
mpirun -n 2 -H 10.45.9.32,10.45.9.30 --allow-run-as-root hostname
```

### Train the model
```
# few output in console while training
nohup mpirun --allow-run-as-root -n 4 -H 10.45.9.32,10.45.9.30 -bind-to none -map-by slot --mca btl_tcp_if_include eth0 -x NCCL_SOCKET_IFNAME=eth0 -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH python run.py --config_file=/data/transformer-base.py --use_horovod=True --mode=train_eval &

# more output in console while training
mpirun --allow-run-as-root -n 4 -H 10.45.9.32:2,10.45.9.30:2 -bind-to none -map-by slot --mca btl_tcp_if_include eth0 -x NCCL_SOCKET_IFNAME=eth0 -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH python /opt/OpenSeq2Seq/run.py --config_file=/data/transformer-base.py --use_horovod=True --mode=train_eval &
```
