```
文件句柄, Linux一切皆文件，文件句柄可以理解为就是一个索引
文件句柄会随着我们进程的调用频繁增加
系统默认对文件句柄有限制，不能让一个进程无限的调用
需要限制每个进程和每个服务使用多大的文件句柄
文件句柄是必须要调整的优化参数


设置方式
系统全局性修改
用户局部性修改
进程局部性修改
```

1. 查看系统默认设置：
```
（1）系统默认的最大值
  file-max是内核可分配的最大文件数
  root@desktop:~# cat /proc/sys/fs/file-max
  6553560


  nr_open是单个进程可分配的最大文件数
  root@desktop:~# cat /proc/sys/fs/nr_open
  1048576


  一般系统默认内核可分配的最大文件数是内存的10%左右，可以调整到50%左右。
  root@desktop:~# grep MemTotal /proc/meminfo | awk '{printf("%d",$2/10)}'
  307462
```


修改系统配置：
vim /etc/security/limits.conf
```
root soft nofile 65535
root hard nofile 65535

```

重启查看ulimit -n  发生变化


vim /etc/security/limits.conf
//针对root用户
root soft nofile 65535
root hard nofile 65535


//所有用户, 全局
* soft nofile 25535
* hard nofile 25535


//对于Nginx进程 worker_rlimit_nofile 65535;


 备注：可以使用ulimit -a 命令查看open files  65535 系统最大打开文件数的值。


 修改前最大打开数为1024
```
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



修改系统文件打开数量后
```
root@desktop:/opt/docker# ab -n 30000 -c 4000  http://192.168.6.92/
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

Concurrency Level:      4000
Time taken for tests:   2.366 seconds
Complete requests:      30000
Failed requests:        0
Non-2xx responses:      30000
Total transferred:      11160000 bytes
HTML transferred:       5070000 bytes
Requests per second:    12680.67 [#/sec] (mean)
Time per request:       315.441 [ms] (mean)
Time per request:       0.079 [ms] (mean, across all concurrent requests)
Transfer rate:          4606.65 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       20  143 178.4    110    1105
Processing:    42  145  45.3    144     317
Waiting:       25  110  44.1    106     288
Total:        105  287 185.6    252    1306

Percentage of the requests served within a certain time (ms)
  50%    252
  66%    270
  75%    285
  80%    298
  90%    326
  95%    351
  98%   1260
  99%   1281
 100%   1306 (longest request)

```


总结：
并发数可以超过1024了，可以实现的并发数量大大增加，但是Requests per second随着并发数增加先增加后减小




修改对一个进程打开的文件句柄数量的限制
```
 echo "* soft nofile 65535"  >> /etc/security/limits.conf
 echo "* hard nofile 65535"  >> /etc/security/limits.conf
```
修改以后保存，注销当前用户，重新登录，执行ulimit -a ,ok ,参数生效了


修改 /etc/sysctl.conf, 加入

fs.file-max = 6553560 重启生效


- [too many files 解决方案](http://blog.itpub.net/25462274/viewspace-2123286/)
- [Linux允许打开最大文件句柄数的参数调优](http://blog.51cto.com/12824426/2060594)
