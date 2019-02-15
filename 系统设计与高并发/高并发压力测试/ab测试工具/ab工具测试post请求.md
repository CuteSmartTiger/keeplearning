##### 针对登录接口的测试


ab -n 500 -c 360 -p ./info.txt -T 'application/json'   'http://192.168.6.92/v2/login'


info.txt
```SHELL
{"username":"admin","password":"123123"}

```

测试结果：
```
root@desktop:~# ab -n 500 -c 380 -p ./info.txt -T 'application/json'   'http://192.168.6.92/v2/login'
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.6.92 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Finished 500 requests


Server Software:        nginx/1.4.6
Server Hostname:        192.168.6.92
Server Port:            80

Document Path:          /v2/login
Document Length:        17 bytes

Concurrency Level:      380
Time taken for tests:   1.345 seconds
Complete requests:      500
Failed requests:        0
Total transferred:      148500 bytes
Total body sent:        91000
HTML transferred:       8500 bytes
Requests per second:    371.64 [#/sec] (mean)
Time per request:       1022.492 [ms] (mean)
Time per request:       2.691 [ms] (mean, across all concurrent requests)
Transfer rate:          107.79 [Kbytes/sec] received
                        66.05 kb/s sent
                        173.84 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    9   5.3     12      14
Processing:    19  546 501.7    284    1323
Waiting:       19  546 501.7    284    1323
Total:         32  556 502.3    296    1335

Percentage of the requests served within a certain time (ms)
  50%    296
  66%   1062
  75%   1117
  80%   1138
  90%   1287
  95%   1313
  98%   1328
  99%   1334
 100%   1335 (longest request)


```
