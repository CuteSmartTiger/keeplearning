- [MySQL高可用架构-MMM环境部署记录](http://www.cnblogs.com/kevingrace/p/5662975.html)

- [MySQL高可用集群之MySQL-MMM](https://blog.csdn.net/bjash/article/details/50475872)

- [mysql MMMM搭建](http://mysql-mmm.org/mmm2:guide#monitoring_host)


初始化数据库


对数据库进行配置


从服务器my.cnf
server-id = 3
log-bin = mysql-bin
log_slave_updates = 1



90上：
stop slave;
GRANT REPLICATION SLAVE ON *.* TO 'root'@'192.168.6.%' IDENTIFIED BY '123123';
FLUSH PRIVILEGES;
show master status;


91上：
CHANGE MASTER TO MASTER_HOST='192.168.6.90',MASTER_USER='root',MASTER_PASSWORD='123123',MASTER_LOG_FILE='mysql-bin.000009',MASTER_LOG_POS=344;

start slave;
SHOW SLAVE STATUS\G
