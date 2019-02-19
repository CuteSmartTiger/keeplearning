```
测试环境：

系统： CentOS 7.1
Mem: 8G
CPU: 虚拟机16核
Python版本： python3.6
Flask版本： 0.12.2
Golang版本： 1.6.3
1.首先写一个Flask的web程序，只返回一个 Hello word!
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello word!'

if __name__ == '__main__':
    app.run()
2.写一个go语言的web程序，也返回一个 Hello word!
package main

import (
    f "fmt"
    "log"
    "net/http"
)

func sayhelloName(w http.ResponseWriter, r *http.Request) {
    f.Fprintln(w, "hello world!")
}
func main() {
    http.HandleFunc("/", sayhelloName)
    err := http.ListenAndServe(":8080", nil)
    if err != nil {
        log.Fatal("ListenAndServe:", err)
    }
}
3.直接在控制台启动Flask, 用压力测试工具模拟并发请求。这里模拟100个并发100000个请求。
ab -n 100000 -c 100 "http://172.30.200.88:5000/"
Server Software:        Werkzeug/0.12.2
Server Hostname:        172.30.200.88
Server Port:            5000

Document Path:          /
Document Length:        11 bytes

Concurrency Level:      100
Time taken for tests:   88.441 seconds
Complete requests:      100000
Failed requests:        0
Write errors:           0
Total transferred:      16500000 bytes
HTML transferred:       1100000 bytes
Requests per second:    1130.70 [#/sec] (mean)
Time per request:       88.441 [ms] (mean)
Time per request:       0.884 [ms] (mean, across all concurrent requests)
Transfer rate:          182.19 [Kbytes/sec] received
4.用Gunicorn以8个进程启动flask，再以同样的并发测试一遍
Server Software:        gunicorn/19.7.1
Server Hostname:        172.30.200.88
Server Port:            8080

Document Path:          /
Document Length:        11 bytes

Concurrency Level:      100
Time taken for tests:   15.842 seconds
Complete requests:      100000
Failed requests:        0
Write errors:           0
Total transferred:      17100000 bytes
HTML transferred:       1100000 bytes
Requests per second:    6312.50 [#/sec] (mean)
Time per request:       15.842 [ms] (mean)
Time per request:       0.158 [ms] (mean, across all concurrent requests)
Transfer rate:          1054.14 [Kbytes/sec] received
5.以同样的并发测试Go
Server Software:        
Server Hostname:        172.30.200.88
Server Port:            8080

Document Path:          /
Document Length:        13 bytes

Concurrency Level:      100
Time taken for tests:   12.460 seconds
Complete requests:      100000
Failed requests:        0
Write errors:           0
Total transferred:      13000000 bytes
HTML transferred:       1300000 bytes
Requests per second:    8025.80 [#/sec] (mean)
Time per request:       12.460 [ms] (mean)
Time per request:       0.125 [ms] (mean, across all concurrent requests)
Transfer rate:          1018.90 [Kbytes/sec] received
测试结果：
Flask 总耗时 88.441秒，平均每秒处理1130个请求
Gunicorn多进程时耗时 15.842， 平均每秒处理 6312个请求
Go 总耗时 12.46秒，每秒处理 8025个请求
```
