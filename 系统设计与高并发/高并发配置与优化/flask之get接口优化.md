get请求的运算时间是0.01s
则QPS最佳的压力测试数据为：
```
root@desktop:/opt/docker# ab -n 1000 -c 100  http://192.168.6.92/v2/users/test
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
Time taken for tests:   1.409 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      276000 bytes
HTML transferred:       5000 bytes
Requests per second:    709.48 [#/sec] (mean)
Time per request:       140.947 [ms] (mean)
Time per request:       1.409 [ms] (mean, across all concurrent requests)
Transfer rate:          191.23 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.7      0       4
Processing:    12  134  22.2    139     147
Waiting:       12  134  22.2    139     147
Total:         16  134  21.5    139     148

Percentage of the requests served within a certain time (ms)
  50%    139
  66%    140
  75%    141
  80%    141
  90%    142
  95%    143
  98%    144
  99%    145
 100%    148 (longest request)

```



将get请求中的运算优化到0.001s，则结果为：
```
root@desktop:/opt/docker# ab -n 1000 -c 100  http://192.168.6.92/v2/users/test
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
Time taken for tests:   0.406 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      276000 bytes
HTML transferred:       5000 bytes
Requests per second:    2463.21 [#/sec] (mean)
Time per request:       40.597 [ms] (mean)
Time per request:       0.406 [ms] (mean, across all concurrent requests)
Transfer rate:          663.91 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.9      0       4
Processing:     6   38   5.8     38      58
Waiting:        6   38   5.8     37      58
Total:         10   39   5.4     38      59

Percentage of the requests served within a certain time (ms)
  50%     38
  66%     39
  75%     40
  80%     42
  90%     46
  95%     48
  98%     51
  99%     53
 100%     59 (longest request)
```

总结：并发用户为100时吞吐率最高，达到2463， 当增加并发用户时为200时，吞吐率降到700左右
