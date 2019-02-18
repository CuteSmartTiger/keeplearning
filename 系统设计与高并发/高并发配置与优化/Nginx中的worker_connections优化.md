worker_connections：

官方解释如下，个人认为是每一个worker进程能并发处理（发起）的最大连接数（包含所有连接数）。

不能超过最大文件打开数：在linux终端中输入ulimit -a进行查看




- 优化前：
```
worker_connections 768；

# 测试结果：

压力测试显示并发上线Concurrency Level值不超过800

root@desktop:/opt/docker/mnt# ab -n 30000 -c 700  http://192.168.6.92/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.6.92 (be patient)
Completed 3000 requests
Completed 6000 requests
Completed 9000 requests
Completed 12000 requests
Completed 15000 requests
Completed 18000 requests
Completed 21000 requests
Completed 24000 requests
Completed 27000 requests
Completed 30000 requests
Finished 30000 requests


Server Software:        nginx/1.4.6
Server Hostname:        192.168.6.92
Server Port:            80

Document Path:          /
Document Length:        169 bytes

Concurrency Level:      700
Time taken for tests:   2.104 seconds
Complete requests:      30000
Failed requests:        0
Non-2xx responses:      30000
Total transferred:      11160000 bytes
HTML transferred:       5070000 bytes
Requests per second:    14255.91 [#/sec] (mean)
Time per request:       49.102 [ms] (mean)
Time per request:       0.070 [ms] (mean, across all concurrent requests)
Transfer rate:          5178.90 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        6   27 102.5     17    1022
Processing:     7   22   7.6     21     216
Waiting:        5   16   6.8     15     212
Total:         19   48 103.6     43    1050

Percentage of the requests served within a certain time (ms)
  50%     43
  66%     47
  75%     49
  80%     50
  90%     51
  95%     53
  98%     55
  99%   1026
 100%   1050 (longest request)
```

优化配置为：

```
worker_connections 10240；

# 测试结果：

压力测试显示并发上线Concurrency Level值不超过1024,ulimit -a分析服务器最大打开的文件句柄为1024

root@desktop:/opt/docker/mnt# ab -n 30000 -c 1020  http://192.168.6.92/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.6.92 (be patient)
Completed 3000 requests
Completed 6000 requests
Completed 9000 requests
Completed 12000 requests
Completed 15000 requests
Completed 18000 requests
Completed 21000 requests
Completed 24000 requests
Completed 27000 requests
Completed 30000 requests
Finished 30000 requests


Server Software:        nginx/1.4.6
Server Hostname:        192.168.6.92
Server Port:            80

Document Path:          /
Document Length:        169 bytes

Concurrency Level:      1020
Time taken for tests:   2.142 seconds
Complete requests:      30000
Failed requests:        0
Non-2xx responses:      30000
Total transferred:      11160000 bytes
HTML transferred:       5070000 bytes
Requests per second:    14006.18 [#/sec] (mean)
Time per request:       72.825 [ms] (mean)
Time per request:       0.071 [ms] (mean, across all concurrent requests)
Transfer rate:          5088.18 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        6   43 146.8     17    1042
Processing:     8   28  15.7     23     218
Waiting:        5   21  12.8     18     216
Total:         18   71 149.7     49    1081

Percentage of the requests served within a certain time (ms)
  50%     49
  66%     71
  75%     74
  80%     76
  90%     81
  95%     96
  98%   1034
  99%   1060
 100%   1081 (longest request)

```

查看服务最大打开文件句柄：open files      (-n) 1024
```

root@desktop:/opt/docker# ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 11852
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 11852
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```


总结：
并发处理数量增加，但是每秒处理的请求数量并没有大幅度增加
