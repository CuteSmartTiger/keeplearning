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

processes = 8
threads = 8
enable-thread = true

logto = /var/log/vdidesktop/vdidesktop.log
log-maxsize = 50000000
disable-logging = true

chmod-socket = 666

```

将processs改为8，则压力测试结果：
```
oot@desktop:~# ab -n 1000 -c 300  http://192.168.6.92/v2/users/test
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

Concurrency Level:      300
Time taken for tests:   1.255 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      276000 bytes
HTML transferred:       5000 bytes
Requests per second:    796.62 [#/sec] (mean)
Time per request:       376.589 [ms] (mean)
Time per request:       1.255 [ms] (mean, across all concurrent requests)
Transfer rate:          214.72 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2   3.5      0      11
Processing:    18  159 285.4     48    1033
Waiting:       18  159 285.4     48    1033
Total:         22  161 285.6     50    1041

Percentage of the requests served within a certain time (ms)
  50%     50
  66%     61
  75%     73
  80%    100
  90%    430
  95%   1020
  98%   1028
  99%   1033
 100%   1041 (longest request)
```

优化配置将threads = 16

测试结果：
```
root@desktop:~# ab -n 1000 -c 300  http://192.168.6.92/v2/users/test
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

Concurrency Level:      300
Time taken for tests:   0.349 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      276000 bytes
HTML transferred:       5000 bytes
Requests per second:    2861.39 [#/sec] (mean)
Time per request:       104.844 [ms] (mean)
Time per request:       0.349 [ms] (mean, across all concurrent requests)
Transfer rate:          771.23 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2   3.4      0      12
Processing:    15   58  21.8     56     255
Waiting:       15   57  21.8     56     255
Total:         15   60  22.1     57     255

Percentage of the requests served within a certain time (ms)
  50%     57
  66%     69
  75%     76
  80%     79
  90%     88
  95%     92
  98%     96
  99%    103
 100%    255 (longest request)
```


提高并发连接的客户端：
```
root@desktop:~# ab -n 10000 -c 3000  http://192.168.6.92/v2/users/test
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.6.92 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        nginx/1.4.6
Server Hostname:        192.168.6.92
Server Port:            80

Document Path:          /v2/users/test
Document Length:        5 bytes

Concurrency Level:      3000
Time taken for tests:   3.987 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      2760000 bytes
HTML transferred:       50000 bytes
Requests per second:    2508.10 [#/sec] (mean)
Time per request:       1196.125 [ms] (mean)
Time per request:       0.399 [ms] (mean, across all concurrent requests)
Transfer rate:          676.01 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   87 228.7      0    1006
Processing:     3  657 854.5    121    3574
Waiting:        3  657 854.5    121    3574
Total:          3  744 886.9    135    3651

Percentage of the requests served within a certain time (ms)
  50%    135
  66%   1052
  75%   1373
  80%   1572
  90%   1894
  95%   2464
  98%   3044
  99%   3610
 100%   3651 (longest request)

```


#### 总结：
1. 吞吐量大概翻了三倍
2. uwsgi中线程的优化可以提高同时连接客户端的数量,可以从几百提高到几千
