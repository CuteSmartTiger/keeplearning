双主参考文章：
http://blog.51cto.com/ygqygq2/1870864

docker volume create v1
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e XTRABACKUP_PASSWORD=123123 -v v1:/var/lib/mysql --name=mysql-A mysql/mysql-server:5.5

进入容器，配置文件/etc/my.cnf
mysql-A配置文件：
skip-host-cache
skip-name-resolve
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
secure-file-priv=/var/lib/mysql-files
user=mysql

# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid



server-id = 1
log-bin = mysql-bin
auto_increment_offset = 1
auto_increment_increment = 2




参考文章地址：https://www.cnblogs.com/phpstudy2015-6/p/6485819.html#_label7
mysql-B配置文件：
server-id = 2
auto_increment_offset = 2
auto_increment_increment = 2
log-bin = mysql-bin



在192.168.6.90上执行mysql语句：
GRANT REPLICATION SLAVE ON *.* TO 'root'@'192.168.6.49' IDENTIFIED BY '123123';
FLUSH PRIVILEGES;

然后数据库中查看二进制文件与位置：
show master status;

在192.168.6.49中执行：
mysql>CHANGE MASTER TO MASTER_HOST='192.168.6.90',MASTER_USER='root',MASTER_PASSWORD='123123',MASTER_LOG_FILE='mysql-bin.000001',MASTER_LOG_POS=345;

start slave;
SHOW SLAVE STATUS\G


在49上：
GRANT REPLICATION SLAVE ON *.* TO 'root'@'192.168.6.90' IDENTIFIED BY '123123';
FLUSH PRIVILEGES;

然后数据库中查看二进制文件与位置：
show master status;


在49上查看二进制文件与位置：
mysql>CHANGE MASTER TO MASTER_HOST='192.168.6.49',MASTER_USER='root',MASTER_PASSWORD='123123',MASTER_LOG_FILE='mysql-bin.000001',MASTER_LOG_POS=107;

分别在192.168.6.49与192.168.6.90中执行mysql语句：
启动
start slave;

查看主从复制配置是否成功：
SHOW SLAVE STATUS\G

两者都为Yes才成功
Slave_IO_Running: Yes
Slave_SQL_Running: Yes

其他双主介绍比较好的文章：
搭建mysql高可用负载均衡集群
https://www.cnblogs.com/phpstudy2015-6/p/6706465.html

生产环境中先运行一个服务器，然后进行数据的初始化，数据会发生同步，所以另外一个服务器不必要进行初始化，否则数据会发生冲突
