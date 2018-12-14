复制性能优化：
- 主库写入二进制日志的时间主库写完后，从库才可以复制，所以将主库的大事物分割为小事物

- 二进制日志传输时间
传输日志量，可以使用mixed日志格式


- 使用多线程复制
stop slave;
set global slave_parallel_type = "logical_clock";
set global slave_parallel_workers =4;
start slave;
