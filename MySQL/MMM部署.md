- [MySQL高可用架构-MMM环境部署记录](http://www.cnblogs.com/kevingrace/p/5662975.html)

初始化数据库




从服务器my.cnf
server-id = 3
log-bin = mysql-bin
log_slave_updates = 1
