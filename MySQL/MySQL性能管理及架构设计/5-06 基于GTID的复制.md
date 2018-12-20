配置主数据库
```
bin_log = /usr/local/mysql/log/mmysql-bin
server_id = 100
#集群中每一个都需要配置
gtid_mode = on
# 强制gtid的一致性
# 开启后不可以有create  或select操作
enfore-gtid-consistency
#启动日志
log-slave-updates = on
```

配置从数据库服务器
```
server_id = 101
relay_log = /usr/local/mysql/log/relay_log
#集群中每一个都需要配置
gtid_mode = on
# 强制gtid的一致性
# 开启后不可以有create  或select操作
enfore-gtid-consistency
#启动日志
log-slave-updates = on

#建议的配置，保证安全性
read_only=on
master_info_repository=TABLE
relay_log_info_repostory =TABLE
```

初始化从服务器数据
mysqldump --master-data=2 --single-transaction

xtrabackup --slave-info
记录备份时最后的事物的GTID值

启动基于GTID的复制过程
```
change master to master_host ="master_host_ip",
master_user = 'repl',
master_password = "password",
master_auto_position =1;
```

##### 演示
配置主从后重启数据库服务器
/etc/init.d/mysql restart


主服务器
初始化数据库并配置触发器
(数据库的版本尽可能一样)
mysqldump  --single-transaction --master-data=2 --trigger --routines --all-databases -uroot -p > a87.sql

将生成的数据库文件从容器复制到宿主机上的指定位置
docker cp 42cbb4ba3f2d9f217611192f81166b236df794d889ca6154a22497383cf60144:/a87.sql /var/

在主服务器上将文件复制从服务器
scp all2.sql root@192.168.3.101:/root


在87主服务器上操作
scp /var/a87.sql root@192.168.6.88:/var

将宿主机的文件复制到容器里
docker cp /var/a87.sql  42cbb4ba3f2d9f217611192f81166b236df794d889ca6154a22497383cf60144:/


优化方向：复制文件时可以把文件复制到宿主机与容器之间自动同步的文件下

在88从服务器上
初始化数据库
mysql -uroot -p < all2.sql

mysql -uroot -p < a87.sql



##### 优缺点
优点：
- 可以很方便的进行故障转移
- 从库不会丢失主库上的任何修改

缺点：
- 故障处理复杂
- 对执行的SQL有一定的限制


##### 如何选择复制模式
- 所使用的MySQL了版本
- 复制架构及主从切换的方式
- 所使用的高可用管理组件
- 对应用的支持程度

#### 推荐文章
- [MySQL5.6 新特性之GTID](https://www.cnblogs.com/zhoujinyi/p/4717951.html)
