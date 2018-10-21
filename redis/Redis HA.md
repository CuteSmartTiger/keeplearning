##Redis 高速缓存
方案一：RedisCluster：官方推荐   没有中心节点
数据可以被分片存储：如果有节点挂了，数据就丢失了，所以需要备份冗余节点，可以分配N个master节点，
N必须为奇数，至少有三个，防止脑裂，再配置N个冗余节点，主从模式下Master/Slave数据存储是完全一
致的），因为Redis集群中3台Master的数据存储并不一样
管理方便：后续可以自行增加或者摘除节点

方案二：Codis：中间件产品，存在中心节点      中心节点宕机就没法用了
方案三：Twemproxy：中间件产品，灿在中心节点   中心节点宕机就没法用了



#### 解除docker集群
docker swarm leave -f
docker network  ls
docker network rm [name]

#####创建net2网络
docker network create --subnet=172.19.0.0/16 net2


#####创建Redis容器
docker run -it -d --name r1 -p 5001:6379 --net=net2 --ip 172.19.0.2 redis bash

配置文件 (需要进入容器)
地址：/usr/redis/redis.conf

主要改的几点内容：
bind 0.0.0.0                       #默认ip为127.0.0.1 需要改为其他节点机器可访问的ip 否则创建集群时无法访问对应的端口，无法创建集群
daemonize yes                      #以后后台运行
cluster-enabled yes                #开启集群
cluster-config-file nodes.conf     # 集群配置文件，集群节点搭建成功后节点的信息所存的文件   nodes这个名字自己可以取
cluster-node-timeout 15000         #节点之间连接超时时间
appendonly yes                     #开启AOF模式，一旦Redis宕机，可以通过日志恢复Redis



修改配置文件后退出容器，然后停止redis节点容器然后再启动
docker stop r1 r2 r3 r4 r5 r6
docker start r1 r2 r3 r4 r5 r6

然后进入每一个容器启动redis
__启动Redis __
进以下目录  /usr/redis/src
输入redis启动命令：
./redis-server ../redis.conf


依次启动其他五个redis节点：

docker run -it -d --name r2 -p 5002:6379 --net=net2 --ip 172.19.0.3 redis bash
docker run -it -d --name r3 -p 5003:6379 --net=net2 --ip 172.19.0.4 redis bash
docker run -it -d --name r4 -p 5004:6379 --net=net2 --ip 172.19.0.5 redis bash
docker run -it -d --name r5 -p 5005:6379 --net=net2 --ip 172.19.0.6 redis bash
docker run -it -d --name r6 -p 5006:6379 --net=net2 --ip 172.19.0.7 redis bash


在r1节点上：
在容器中将redis-trib.rb 复制到一个空文件，这个空文件(/usr/redis/cluster/)可以自己创建
cp /usr/redis/src/redis-trib.rb /usr/redis/cluster/


然后进入cluster目录下：
安装ruby
apt-get install ruby
apt-get install rubygems
gem install redis


进入redis-trib.rb所在的cluster目录下：
./redis‐trib.rb create --replicas 1 172.19.0.2:6379 172.19.0.3:6379 172.19.0.4:6379 172.19.0.5:6379 172.19.0.6:6379 172.19.0.7:6379
--replicas 1 代表为每一个主节点创造一个从节点
--replicas 2 意思为为每个 master 分配 2 各 slave，replicas表示需要有几个slave。不填写这个参数是可以创建成功的，这样是三个master


进入r1节点：
docker exec -it r1 bash

使用redis命令工具：
/usr/redis/src/redis-cli -c
-c 表示连接redis集群

redis写入数据：
set a liuhu

redis 获取数据
get a

测试主从情况：
暂停一个容器：
docker pause r3

重启一个容器节点
docker unpause r3
重启后此节点从master降为salve


查看集群点状态
cluster nodes
