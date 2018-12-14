##### 基于段的格式
binlog_format=statement;

查看二进制日志格式
show variables like "binlog_format";

将二进制日志格式设置为段的格式
set session binlog_format=statement;

查看二进制日志
show binary logs;

刷新日志
flush logs;

进入查看日志的目录
cd /home/mysql/sql_log

ls -lh

mysqlbinlog mysql-bin.000002

- 优点

- 缺点

##### 基于行的日志格式（推荐）
binlog_format =ROW

- 优点
  - 主从复制更加安全
  - 对每行数据的修改比基于段的复制高效
  - 在没备份的情况下可以通过分析日志知道针对每行的操作（万不得已）

- 缺点
  - 记录日志量大
  binlog_row_image = [FULL|MINIMAL|NOBLOG]

- 调试
将二进制日志格式设置为row的格式
set session binlog_format=row;

查看二进制日志格式,修改是否成功
show variables like "binlog_format";

刷新日志
flush logs;

查看日志存储方式
show variable like "binlog_row_image";


进入查看日志的目录
cd /home/mysql/sql_log

ls -lh

mysqlbinlog mysql-bin.000003

mysqlbinlog -vv mysql-bin.000003 | more

设置日志存储格式
set session binlog_row_image=minimal;


##### 混合日志格式
binlog_format=MIXED

特点：
- 根据SQL语句有系统决定基于段和基于行的日志中选择进行
- 数据量的大小有所执行的sql语句决定


##### 选择
方案一：
binlog_format = mixed

方案二：
binlog_format = row
同时
binlog_row_image=minimal
