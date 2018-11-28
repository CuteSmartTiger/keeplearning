#### 集群完整性
cluster-require-full-coverage yes
生产环境必须是no，否则有宕机出现槽缺失的时候集群会失效

调试关节点的命令
redis-cli -p 9000 shutdown

#### 带宽消耗
官方建议：不超过1000节点
消耗带宽


#### pub/sub广播
面临的问题：发布消息时，要通知其他节点，节点面临的带宽消耗会很大


#### 数据倾斜
- 节点与槽的分配不均
redis-trib.rb info ip:port 查看节点、槽、键值分布
redis-trib.rb rebalance ip:port 进行均衡（谨慎使用）

- 不同槽对应键值数量差异比较大
CRC16正常情况下比较均匀
可能存在hash_tag
cluster countkeysinsolt {slot} 获取槽对应键值个数

- 包含bigkey
bigkey：例如大字符串 、几百万的元素的hash 、set等
从节点执行：redis-cli --bigkeys
优化：优化数据结构


- 内存相关配置不一致
hash-max-ziplist-value 、set-max-intset-entries
优化：定期检查配置一致性


- 读写分离（集群下不建议使用）



- 数据迁移


- 集群VS单机
