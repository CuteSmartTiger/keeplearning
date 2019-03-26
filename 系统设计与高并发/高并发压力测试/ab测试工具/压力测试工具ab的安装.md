先更新源

sudo apt-get install apache2
或
ubuntu:sudo apt-get install apache2-utils

centos：yum install httpd-tools


sudo /etc/init.d/apache2 restart

ab -V

ab -n 100 -c 100 http://192.168.6.92/admin/home



简易化安装脚本：
```SHELL
#! /bin/bash
dns-nameserver 8.8.8.8 > /etc/network/interfaces


sudo mv /var/lib/dpkg/info  /var/lib/dpkg/info_old
sudo mkdir /var/lib/dpkg/info
sudo apt-get update
sudo apt-get -f install
sudo mv /var/lib/dpkg/info/*   /var/lib/dpkg/info_old
sudo rm -rf  /var/lib/dpkg/info
sudo mv  /var/lib/dpkg/info_old  /var/lib/dpkg/info

sudo apt-get update
sudo apt-get -y install percona-toolkit

sudo apt-get install apache2-utils

```







示例
```
root@desktop:~# ab -n 3000 -c 700  http://192.168.6.92/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.6.92 (be patient)
Completed 300 requests
Completed 600 requests
Completed 900 requests
Completed 1200 requests
Completed 1500 requests
Completed 1800 requests
Completed 2100 requests
Completed 2400 requests
Completed 2700 requests
Completed 3000 requests
Finished 3000 requests


Server Software:        nginx/1.4.6
Server Hostname:        192.168.6.92
Server Port:            80

Document Path:          /
Document Length:        169 bytes

Concurrency Level:      700
Time taken for tests:   0.241 seconds
Complete requests:      3000
Failed requests:        0
Non-2xx responses:      3000
Total transferred:      1116000 bytes
HTML transferred:       507000 bytes
Requests per second:    12461.32 [#/sec] (mean)
Time per request:       56.174 [ms] (mean)
Time per request:       0.080 [ms] (mean, across all concurrent requests)
Transfer rate:          4526.96 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        2    7   5.9      4      25
Processing:     2    9   7.6      7     197
Waiting:        1    8   7.2      5     197
Total:          6   16  11.6     10     202

Percentage of the requests served within a certain time (ms)
  50%     10
  66%     11
  75%     24
  80%     26
  90%     34
  95%     40
  98%     43
  99%     45
 100%    202 (longest request)
```
