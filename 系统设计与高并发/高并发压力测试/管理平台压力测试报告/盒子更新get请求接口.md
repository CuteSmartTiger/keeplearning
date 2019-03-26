服务器配置：
ubutu16.4系统
内存：4
CPU：4



ab -n 10 -c 10  "http://192.168.6.87/v2/packages/?mark_latest=1&type=1"


ab -n 500 -c 100  "http://192.168.6.87/v2/packages/?mark_latest=1&type=1"
-c 并发数100或者50测试报告的吞吐量均为100左右
测试结果：
```
root@desktop:~# ab -n 500 -c 50  "http://192.168.6.87/v2/packages/?mark_latest=1&type=1"
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.6.87 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Finished 500 requests


Server Software:        nginx/1.4.6
Server Hostname:        192.168.6.87
Server Port:            80

Document Path:          /v2/packages/?mark_latest=1&type=1
Document Length:        489 bytes

Concurrency Level:      50
Time taken for tests:   4.955 seconds
Complete requests:      500
Failed requests:        0
Total transferred:      395000 bytes
HTML transferred:       244500 bytes
Requests per second:    100.92 [#/sec] (mean)
Time per request:       495.459 [ms] (mean)
Time per request:       9.909 [ms] (mean, across all concurrent requests)
Transfer rate:          77.86 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.0      0       5
Processing:    61  470  87.2    489     573
Waiting:       61  470  87.2    489     573
Total:         66  470  86.3    489     573

Percentage of the requests served within a certain time (ms)
  50%    489
  66%    506
  75%    514
  80%    523
  90%    536
  95%    550
  98%    564
  99%    568
 100%    573 (longest request
```
