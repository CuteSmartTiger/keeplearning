- mysql 配置文件的优化之max_connections

指定MySQL允许的最大连接进程数,若经常出现Too Many Connections的错误提示，则需要增大该参数值。
max_connections=1000;
```

set global max_connections=100;
SHOW VARIABLES LIKE 'max_connections';

root@007490428b22:/#  mysqlslap -a -c 300 -i 10 -uroot -p123123
mysqlslap: [Warning] Using a password on the command line interface can be insecure.
Benchmark
	Average number of seconds to run all queries: 0.827 seconds
	Minimum number of seconds to run all queries: 0.741 seconds
	Maximum number of seconds to run all queries: 0.939 seconds
	Number of clients running queries: 300
	Average number of queries per client: 0



set global max_connections=400;
SHOW VARIABLES LIKE 'max_connections';

root@007490428b22:/#  mysqlslap -a -c 500 -i 10 -uroot -p123123
mysqlslap: [Warning] Using a password on the command line interface can be insecure.
mysqlslap: Error when connecting to server: 1040 Too many connections
mysqlslap: Error when connecting to server: 1040 Too many connections
mysqlslap: Error when connecting to server: 1040 Too many connections
mysqlslap: Error when connecting to server: 1040 Too many connections
Benchmark
	Average number of seconds to run all queries: 1.780 seconds
	Minimum number of seconds to run all queries: 1.696 seconds
	Maximum number of seconds to run all queries: 1.957 seconds
	Number of clients running queries: 500
	Average number of queries per client: 0


set global max_connections=1000;
SHOW VARIABLES LIKE 'max_connections';

root@007490428b22:/#  mysqlslap -a -c 500 -i 10 -uroot -p123123
mysqlslap: [Warning] Using a password on the command line interface can be insecure.
Benchmark
	Average number of seconds to run all queries: 1.803 seconds
	Minimum number of seconds to run all queries: 1.610 seconds
	Maximum number of seconds to run all queries: 2.150 seconds
	Number of clients running queries: 500
	Average number of queries per client: 0


set global max_connections=1000;
SHOW VARIABLES LIKE 'max_connections';

root@007490428b22:/#  mysqlslap -a -c 1000 -i 10 -uroot -p123123
mysqlslap: [Warning] Using a password on the command line interface can be insecure.
Benchmark
	Average number of seconds to run all queries: 5.700 seconds
	Minimum number of seconds to run all queries: 5.260 seconds
	Maximum number of seconds to run all queries: 6.573 seconds
	Number of clients running queries: 1000
	Average number of queries per client: 0

```
