持久化概念
将内存数据异步保存到磁盘中


主流方法：
快照    Redis RDB,MySQL Dump，
写日志  Redis AOF,Hbase Hlog，MySQL Binlog，



####
RDB文件，二进制


- save 同步
缺点：阻塞

文件策略：替换
复杂度：n




- bgsave 异步
返回：backgroud saving started





- 自动
设置配置文件
缺点：频率太高

dbfilename dump-${port}.rdb
dir /bigdiskpath
stop-writes-on-bgsave-error yes
rdbcompression yes


#### 触发机制-不可忽略方式
全量复制
debug reload
shutdown


```
dbfilename dump-6379.rdb

dir /opt/soft/redis/data

```

启动配置文件
redis-server  redis.conf


启动客户端：
