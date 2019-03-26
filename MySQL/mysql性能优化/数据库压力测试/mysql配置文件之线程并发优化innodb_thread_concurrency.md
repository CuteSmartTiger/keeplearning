MYSQL5.7

提高线程并发数有效果，当
set global innodb_thread_concurrency=16;
测试为：
  ```
  oot@a28f96389392:/# mysqlslap -a -c 400 -i 10 -uroot -p123123
  mysqlslap: [Warning] Using a password on the command line interface can be insecure.
  Benchmark
  	Average number of seconds to run all queries: 1.002 seconds
  	Minimum number of seconds to run all queries: 0.963 seconds
  	Maximum number of seconds to run all queries: 1.109 seconds
  	Number of clients running queries: 400
  	Average number of queries per client: 0

  ```



  当改为：set global innodb_thread_concurrency=4;
  mysqlslap: Error when connecting to server: 1040 Too many connections


- thread_concurrency
  ```
  innodb_thread_concurrency=4
  #该参数取值为服务器逻辑CPU数量*2，在本例中，服务器有2颗物理CPU，而每颗物理CPU又支持H.T超线程，所以实际取值为4*2=8

  改之前没有配置，测试结果如下：
  root@007490428b22:/# mysqlslap -a -c 300 -i 10 -uroot -p123123
  mysqlslap: [Warning] Using a password on the command line interface can be insecure.
  Benchmark
    Average number of seconds to run all queries: 0.866 seconds
    Minimum number of seconds to run all queries: 0.782 seconds
    Maximum number of seconds to run all queries: 1.044 seconds
    Number of clients running queries: 300
    Average number of queries per client: 0


  更该配置为：
  set global innodb_thread_concurrency=4;

  SHOW VARIABLES LIKE 'innodb_thread_concurrency';

  mysqlslap -a -c 300 -i 10 -uroot -p123123
  mysqlslap: [Warning] Using a password on the command line interface can be insecure.
  Benchmark
    Average number of seconds to run all queries: 1.455 seconds
    Minimum number of seconds to run all queries: 1.383 seconds
    Maximum number of seconds to run all queries: 1.591 seconds
    Number of clients running queries: 300
    Average number of queries per client: 0


  更该配置为：
  set global innodb_thread_concurrency=128;

  SHOW VARIABLES LIKE 'innodb_thread_concurrency';

  root@007490428b22:/#  mysqlslap -a -c 300 -i 10 -uroot -p123123
  mysqlslap: [Warning] Using a password on the command line interface can be insecure.
  Benchmark
    Average number of seconds to run all queries: 0.805 seconds
    Minimum number of seconds to run all queries: 0.753 seconds
    Maximum number of seconds to run all queries: 0.890 seconds
    Number of clients running queries: 300
    Average number of queries per client: 0


  更该配置为：
  set global innodb_thread_concurrency=256;

  SHOW VARIABLES LIKE 'innodb_thread_concurrency';

  root@007490428b22:/#  mysqlslap -a -c 300 -i 10 -uroot -p123123
  mysqlslap: [Warning] Using a password on the command line interface can be insecure.
  Benchmark
    Average number of seconds to run all queries: 0.810 seconds
    Minimum number of seconds to run all queries: 0.746 seconds
    Maximum number of seconds to run all queries: 0.900 seconds
    Number of clients running queries: 300
    Average number of queries per client: 0




  增加并发到500则失败
  mysqlslap -a -c 500 -i 10 -uroot -p123123
  ```




- 说明
```

#通过设置配置参数innodb_thread_concurrency来限制并发线程的数量，

#一旦执行线程的数量达到这个限制，额外的线程在被放置到对队列中之前，会睡眠数微秒，

#可以通过设定参数innodb_thread_sleep_delay来配置睡眠时间

#该值默认为0,在官方doc上，对于innodb_thread_concurrency的使用，也给出了一些建议:

#(1)如果一个工作负载中，并发用户线程的数量小于64，建议设置innodb_thread_concurrency=0；

#(2)如果工作负载一直较为严重甚至偶尔达到顶峰，建议先设置innodb_thread_concurrency=128,

###并通过不断的降低这个参数，96, 80, 64等等，直到发现能够提供最佳性能的线程数

#innodb_thread_concurrency = 0

```
