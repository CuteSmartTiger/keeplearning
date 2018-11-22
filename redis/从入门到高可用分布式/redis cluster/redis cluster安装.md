#### 原生命令安装
```
1. 配置开启节点
cluster-enabled ys
cluster-node-timeout 15000
cluster-config-file "nodes.conf"
#一个节点出问题则集群不可用
cluster-require-full-coverage yes
```

2. meet
cluster meet ip port
```
redis-cli -h 127.0.0.1 -p 7000 cluster meet 127.0.0.1 7001
redis-cli -h 127.0.0.1 -p 7000 cluster meet 127.0.0.1 7002
redis-cli -h 127.0.0.1 -p 7000 cluster meet 127.0.0.1 7003
redis-cli -h 127.0.0.1 -p 7000 cluster meet 127.0.0.1 7004
redis-cli -h 127.0.0.1 -p 7000 cluster meet 127.0.0.1 7005
```


3. 指派槽
```
redis-cli -h 127.0.0.1 -p 7001 cluster addslots {}
redis-cli -h 127.0.0.1 -p 7001 cluster addslots {}
redis-cli -h 127.0.0.1 -p 7001 cluster addslots {}
```



4. 主从关系的分配
cluster replication node-id
```
redis-cli -h 127.0.0.1 -p 7003 cluster replicate ${node-id-7000}
redis-cli -h 127.0.0.1 -p 7004 cluster replicate ${node-id-7001}
redis-cli -h 127.0.0.1 -p 7005 cluster replicate ${node-id-7002}
```

#### 单机具体配置
vim redis-7000.conf
```
port 7000
daemonize yes
dir "/opt/soft/redis-5.0.0/data"
logfile "7000.log"
dbfilename "dump-7000.rdb"
cluster-enabled yes
cluster-config-file nodes-7000.conf
cluster-require-full-coverage no
```
cat redis-7000.conf

快速生成其他配置文件：
sed 's/7000/7001/g' redis-7000.conf > redis-7001.conf
sed 's/7000/7002/g' redis-7000.conf > redis-7002.conf
sed 's/7000/7003/g' redis-7000.conf > redis-7003.conf
sed 's/7000/7004/g' redis-7000.conf > redis-7004.conf
sed 's/7000/7005/g' redis-7000.conf > redis-7005.conf

启动：
redis-server redis-7000.conf
ps -ef | grep redis

redis-server redis-7001.conf
redis-server redis-7002.conf
redis-server redis-7003.conf
redis-server redis-7004.conf
redis-server redis-7005.conf
ps -ef | grep redis

测试是否可以添加数据,可以发现还没配置槽时会报错，配置槽后才可以对外服务
redis-cli -p 7000
set liu hu
(error) CLUSTERDOWN Hash slot not served

进入目录下查看日志及节点配置
/opt/soft/redis-5.0.0/data
cat nodes-7001.conf
或者
redis-cli -p 7000 cluster nodes

查看集群信息
redis-cli -p 7000 cluster info
```
cluster_state:fail
cluster_slots_assigned:0
cluster_slots_ok:0
cluster_slots_pfail:0
cluster_slots_fail:0
cluster_known_nodes:1
cluster_size:0
cluster_current_epoch:0
cluster_my_epoch:0
cluster_stats_messages_sent:0
cluster_stats_messages_received:0
```


#### meet 操作
redis-cli -p 7000 cluster meet 127.0.0.1 7001
redis-cli -p 7000 cluster nodes
redis-cli -p 7001 cluster nodes

redis-cli -p 7000 cluster meet 127.0.0.1 7002
redis-cli -p 7000 cluster meet 127.0.0.1 7003
redis-cli -p 7000 cluster meet 127.0.0.1 7004
redis-cli -p 7000 cluster meet 127.0.0.1 7005

redis-cli -p 7000 cluster nodes
redis-cli -p 7000 cluster info


#### 分配槽
redis目录下：
mkdir script
cd script
vim addslots.sh
```
start=$1
start=$2
port=$3
for slot in `seq ${start} ${end}`
do
  echo "slot:${slot}"
  redis-cli -p ${port} cluster addslots ${slot}
done
```
sh addslots.sh 0 5461 7000

redis-cli -p 7000

cluster info
cluster nodes

sh addslots.sh 5462 10922 7001

获取配置文件中的匹配信息
config get cluster*

sh addslots.sh 10923 16383 7002


#### 进行主从分配
查看节点信息
redis-cli -p 7000 cluster nodes

配置从主
redis-cli -p 7003 cluster replicate master_id
redis-cli -p 7000 cluster nodes

以槽为单位查看
redis-cli -p 7000 cluster slots

redis-cli -c -p 7000
