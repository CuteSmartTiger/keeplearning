#### 典型场景
- 缓存器


- 计数器
转发与评论数量

- 消息队列


- 排行榜


- 社交网络


- 实时系统
过滤器


#### Redis安装
下载包
wget

解压
tar -xzf redis-3.0.7.tar.gz

建立软连接，方便以后升级
ln -s redis-3.0.7 Redis

cd redis

编译与安装
make&&make install


#### Redis可执行文件说明
redis-server    redis服务器
redis-cli       Redis命令行客户端
redis-benchmark  redis性能测试

redis-check-aof AOF文件修复工具
redis-check-dump RDB文件检查工具

redis-sentinel（v2.8）支持高可用
redis-cluster（v3.0）支持分布式

#### 启动方法
- 最简启动
启动
redis-server

验证
ps -ef |grep redis

netstat -antpl | grep redis

redis-cli -h ip -p port ping

示例：
redis-cli -h 10.10.79.150 -p 6384
ping
set key value
get key

- 动态启动
默认端口6379
redis-server --port 6380

- 配置文件启动（推荐）
redis-server configPath


#### 客户端返回值
状态回复 PONG
错误回复 error
整数回复 incr hello
字符串回复 get hello
多行字符串回复 mget key1 key2


#### 常用配置
daemonize  是否守护进程（no|Yes）  推荐yes
port        redis对外端口
logfile     redis系统日志
dir         redis工作目录

查看配置
redis-server
config get *

去除配置文件中的指定内容然后重定向输出
cat redis-6381.conf | grep -v "#" | grep -v "^$" > redis-6382.conf

配置内容
```
daemonize yes
port 6382
dir "/opt/soft/redis/data"
logfile "6382.log"

```


启动配置文件
redis-server config/redis-6382.conf

查看是否启动
ps -ef | grep redis-server | grep 6382
