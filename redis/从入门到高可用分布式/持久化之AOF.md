#### RDB问题：
- 耗时 耗性能
- 不可控 丢失数据


#### AOF运行原理
日志文件


#### AOF 策略

- always


- everysec
丢失一秒数据


- no
有操作系统决定
不可控
不管用

#### 面临问题
- AOF重写
优化数据，重复数据，避免AOF文件不断增大
减少硬盘占用量
加速恢复速度

重写方式一：
bgrewriteaof


重写方式二：
AOF重写配置
```
appendonly yes
appendfilename "appendonly=${port}.aof"
appendfsync everysec
dir /bigdiskpath
no-appendfsync-on-rewrite yes
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

```


#### redis支持动态写入：
config get appendonly
config set appendonly yes
