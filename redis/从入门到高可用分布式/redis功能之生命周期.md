#### 慢查询
- 生命周期
1. 发送命令
2. 排队
3. 执行
4. 返回

两点：
慢查询发生在第三阶段
客户端超时不一定慢查询，但慢查询是客户端超时的一个可能因素


两个配置：
先进先出
固定长度
保存在内存中

慢查询阈值（单位：微妙）
默认配置：
config get slowlog-max-len =128
config get slowlog-log-slower-than =10000


动态配置：
config get slowlog-max-len 1000
config get slowlog-log-slower-than 1000


慢查询的命令：
获取慢查询的队列，n指条数
slowlog get [n]

获取安查询的队列长度
slowlog len

清空慢查询队列
slowlog reset


#### 运维经验
slowlog-max-len 不要社会组过大，默认10ms，通常设置1ms
slowlog-log-slower-than 不要设置过小，通常1000左右
定期持久化慢查询
理解命令生命周期


#### 重点
深度理解慢查询所在生命周期的阶段
