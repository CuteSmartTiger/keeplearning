#### 伸缩原理



#### 扩容原理

- 准备新的节点
要求：
集群模式
配置和其他节点统一
启动后是孤儿节点

redis-server conf/redis-6385.conf
redis-server conf/redis-6386.conf

- 加入集群
执行meet操作
127.0.0.1:6379> cluster meet 127.0.0.1:6385
127.0.0.1:6379 > cluster meet 127.0.0.1:6386

查看界节点是否成功
127.0.0.1:6386>clustr nodes

作用：
为他迁移槽与数据实现扩容
作为从节点负责故障转移

推荐使用官方工具加入集群，可以在执行加入时对节点进行检测其是否已经加入集群
前者为新节点后者为已存在的节点
redis-trib.rb add-node 127.0.0.1:6385 127.0.0.1:6379

- 迁移槽与数据

槽迁移计划

迁移数据

添加从节点

sed 's/7000/7006/g' redis-7000.conf > redis-7006.conf
sed 's/7000/7007/g' redis-7000.conf > redis-7007.conf

查看配置是否生效
cat redis-7006.conf

启动服务，并查看是否孤立状态
redis-server redis-7006.conf
redis-server redis-7007.conf


meet操作
redis-cli -p 7000 cluster meet 127.0.0.1 7006
redis-cli -p 7000 cluster nodes

redis-cli -p 7000 cluster meet 127.0.0.1 7007
redis-cli -p 7000 cluster nodes

分配主从关系
redis-cli -p 7007 cluster replicate node_id



集群扩容
src目录下
旧版本命令
./redis-trib.rb reshard 127.0.0.1:7000

新版本命令：
redis-cli --cluster reshard 127.0.0.1:7000
4096
7006_node_id
all
yes

查看迁移情况
redis-cli -p 7000 cluster slots

redis-cli -p 7000 cluster nodes | grep master

#### 缩容集群
- 先迁移槽
ps -ef | grep redis-server | grep 700
redis-cli -p 7000 cluster nodes

先迁移槽
老版本
src目录下：
./redis-trib.rb reshared --from 7006_node_id --to 7000_node_id --slots 1366 127.0.0.1:7006
yes

新版本：
redis-cli --cluster reshard  --cluster-from 7006_node_id  --cluster-to  7000_node_id --cluster-slots  1366 127.0.0.1:7006

redis-cli -p 7000 cluster nodes

redis-cli --cluster reshard  --cluster-from 7006_node_id  --cluster-to  7001_node_id --cluster-slots  1366 127.0.0.1:7006

redis-cli -p 7000 cluster nodes

redis-cli --cluster reshard  --cluster-from 7006_node_id  --cluster-to  7002_node_id --cluster-slots  1366 127.0.0.1:7006

- 然后删除节点
先下从节点再下主节点
老版本：
./redis-trib.rb del-node 127.0.0.1:7000 7007_node_id

新版本：
删除从节点
redis-cli --cluster del-node 127.0.0.1:7000 7007_node_id

查看是否存在
redis-cli -p 7007

删除主节点
redis-cli --cluster del-node 127.0.0.1:7000 7006_node_id
