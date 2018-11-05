### 优化考虑点：
- 1.当前系统的结构瓶颈
观察指标 压力测试

- 2.了解业务模式
接口业务类型，系统层次化结构

- 3.性能与安全


### ab接口压力测试工具
安装

使用
ab -n 2000 -c 2 http://127.0.0.1/
-n 总的请求次数
-c 并发数
-k 是否开启长连接

### 系统与Nginx的性能优化
网络
系统
服务
程序
数据库、底层服务

- 文件句柄
vi /etc/security/limits.conf
添加内容：
```
root soft nofile 65535
root hard nofile 65535
*    soft nofile 65535
*    hard nofile 65535
```

针对Nginx进程的文件句柄进行限制
vi /etc/nginx/nginx.conf
```
worker_rlimit_nofile 35535;
```

需要理解文件句柄的含义：
