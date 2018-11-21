#### 8.6 sentinel主要配置(需要先配置好主从节点)
```
port ${port}
daemonize yes
dir "/opt/soft/redis/data/"
logfile "${port}.log"
#其中的2代表有两个sentinel检具认为宕机则执行后续事宜
sentinel monitor mymaster 127.0.0.1 7000 2
sentinel down-after-milliseconds mymaster 30000
# 参数1，减轻master的压力
sentinel parallel-syncs mymaster 1
sentinel failover-timeout mymaster 180000
```

实例：
```
port 26379
# yes,否则难以启动
daemonize yes
dir /opt/soft/redis/data/
logfile "26379.log"
#其中的2代表有两个sentinel检具认为宕机则执行后续事宜
sentinel monitor mymaster 127.0.0.1 7000 2
sentinel down-after-milliseconds mymaster 30000
# 参数1，减轻master的压力
sentinel parallel-syncs mymaster 1
sentinel failover-timeout mymaster 180000
```

sentinel会通过master节点发现其他slave

启动
redis-sentinel redis-sentinel-26379.conf

redis-cli -p 26379

ping

info


sed "s/26379/26380/g" redis-sentinel-26379.conf > redis-sentinel-26380.conf
sed "s/26379/26381/g" redis-sentinel-26379.conf > redis-sentinel-26381.conf



启动
redis-sentinel redis-sentinel-26380.conf
redis-sentinel redis-sentinel-26381.conf

ps -ef | grep redis-sentinel


redis-cli -p 26380 info sentinel


#### 8.5
主节点配置：
```
port 7000
daemonize yes
pifile /var/run/redis-7000.pid
logfile "7000.log"
dir "/opt/soft/redis/redis/data/"

```


sed "s/7000/7001/g" redis-7000.conf > redis-7001.conf
sed "s/7000/7002/g" redis-7000.conf > redis-7002.conf

echo "slaveof 127.0.0.1 7000" >> redis-7001.conf
echo "slaveof 127.0.0.1 7000" >> redis-7002.conf

快速启动
redis-server redis-7000.conf

检测7000是否启动
redis-cli -p 7000 ping
出现PONG则已启动

redis-server redis-7001.conf
redis-server redis-7002.conf

检测三个进程是否已经启动
ps -ef | grep redis-server | grep 700

查看主从复制的关系
redis-cli -p 7000 info replication
