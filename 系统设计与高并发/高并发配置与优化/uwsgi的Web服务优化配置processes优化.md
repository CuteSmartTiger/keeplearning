优化前的uwsgi配置:
```

[uwsgi]
env = PYTHONIOENCODING=UTF-8
; socket = /tmp/uwsgi.sock
socket = localhost:11000


vacuum = true

module = app:application

virtualenv = flask/
master = true

# 优化前为4，代表同时开启4个web进程响应与处理请求，实际机器为8核
processes = 4
threads = 8
enable-thread = true

logto = /var/log/vdidesktop/vdidesktop.log
log-maxsize = 50000000
disable-logging = true

chmod-socket = 666

```

将processs改为8，则压力测试结果：
```
root@desktop:~# ab -n 1000 -c 100  http://192.168.6.92/v2/users/test
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.6.92 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        nginx/1.4.6
Server Hostname:        192.168.6.92
Server Port:            80

Document Path:          /v2/users/test
Document Length:        5 bytes

Concurrency Level:      100
Time taken for tests:   0.256 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      276000 bytes
HTML transferred:       5000 bytes
Requests per second:    3910.97 [#/sec] (mean)
Time per request:       25.569 [ms] (mean)
Time per request:       0.256 [ms] (mean, across all concurrent requests)
Transfer rate:          1054.13 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.8      0       4
Processing:     5   24   9.7     23      95
Waiting:        5   24   9.7     23      95
Total:          5   25   9.8     24      95

Percentage of the requests served within a certain time (ms)
  50%     24
  66%     27
  75%     29
  80%     31
  90%     37
  95%     41
  98%     49
  99%     57
 100%     95 (longest request)
```
#### 总结：
优化前的吞吐量为两千多点，优化后提高到将近4000，效果非常明显

补充说明：processs数不高于为服务器实际虚拟内核数量，优化uwsgi需要本身机器存在可以优化的空间

Nginx中优化进程数没有效果
