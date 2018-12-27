##### 配置相关
server-id 必须保证每个服务器不一样。 这可能和循环同步有关。 防止进入死循环。
replicate-do-db 可以指定需要复制的数据库， 我这里注掉了。 演示一下。
replicate-ignore-db 复制时需要排除的数据库， 我使用了，这个。 除开系统的几个数据库之外，所有的数据库都复制。
relay_log 中继日志的名字。 前面说到了， 复制线程需要先把远程的变化拷贝到这个中继日志中， 在执行。
log-slave-updates 意思是，中继日志执行之后，这些变化是否需要计入自己的binarylog。 当你的B服务器需要作为另外一个服务器的主服务器的时候需要打开。  就是双主互相备份，或者多主循环备份。 我们这里需要， 所以打开。


##### 参考文件
- [mysql 主从复制 双主从复制原理 防止主键重复问题](https://blog.csdn.net/l192168134/article/details/75601773)



##### 主从复制相关：
Slave_IO_Running：连接到主库，并读取主库的日志到本地，生成本地日志文件
Slave_SQL_Running:读取本地日志文件，并执行日志里的SQL命令。



#### 参考文章
- [数据库主从复制中继日志](https://blog.csdn.net/xuexiaoyaani/article/details/80635122)
