#### 判断是否大量延迟
主上的二进制日志文件名和偏移量
show master status \G
show slave status \G

已经传输完成的日志与偏移量
exec_MASTER_LOG_POS:
relay_log_space:

#### 每次修复主从复制需要检查主从的数据一致性
GRANT  SELECT,PROCESS,SUPER,REPLICATION SLAVE ON *.* TO 'root'@'192.168.6.49' IDENTIFIED BY '123123';


只需要在主库上执行
pt-table-checksum u=root,p='123123' --databases mysql --replicate test.checksums
指定检查的数据，然后将结果写入replicate指定的表中
