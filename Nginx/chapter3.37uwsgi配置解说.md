进入opt/app/conf/目录下：
vim uwsgi.ini

配置：
```
[uwsgi]
socket = 127.0.0.1:9999
#plugin = python
#chdir = /opt/app/code6/demo
#wsgi-file = cms/wsgi.py
processes = 4
#threads = 4
max-request = 1000
#log-x-forwarded-for = true
daemonize = /var/log/uwsgi.log
#logto = /code/uwsgi_web.log
#stats = 127.0.0.1:9191
#确认配置目录存在且有写入权限
pidfile= /var/run/uwsgi/uwsgi.pid
buffer-size = 30000
```

选项解析：
```
socket ： 地址和端口号，例如：socket = 127.0.0.1:50000
processes ： 开启的进程数量
workers ： 开启的进程数量，等同于processes（官网的说法是spawn the specified number ofworkers / processes）
chdir ： 指定运行目录（chdir to specified directory before apps loading）
wsgi-file ： 载入wsgi-file（load .wsgi file）
stats ： 在指定的地址上，开启状态服务（enable the stats server on the specified address）
threads ： 运行线程。由于GIL的存在，我觉得这个真心没啥用。（run each worker in prethreaded mode with the specified number of threads）
master ： 允许主进程存在（enable master process）
daemonize ： 使进程在后台运行，并将日志打到指定的日志文件或者udp服务器（daemonize uWSGI）。实际上最常用的，还是把运行记录输出到一个本地文件上。
pidfile ： 指定pid文件的位置，记录主进程的pid号。
vacuum ： 当服务器退出的时候自动清理环境，删除unix socket文件和pid文件（try to remove all of the generated file/sockets）
disable-logging ： 不记录请求信息的日志。只记录错误以及uWSGI内部消息到日志中。如果不开启这项，那么你的日志中会大量出现这种记录：

```
启用uws进程时先确保进程关闭
查看进程：
ps -ef|grep uwsgi


启用进程：
/opt/python3.6/bin/uwsgi --ini ./uwsgi.ini
可以根据日志与查看进程确认是否启动成功与查找错误




查看Nginx反向代理配置：
cat /etc/nginx/conf.d/uwsgi.conf

示例代码：
```
server {
    listen 8090;
    server_name 1.test.com;
    charset     utf-8;

    location / {
      include uwsgi_params;
      #uwsgi_pass unix:/tmp/uwsgi.sock;
      uwsgi_pass 127.0.0.1:9999;
      #‘.’作为分隔符，实际含义为demo目录下的wsgi.py文件
      uwsgi_param UWSGI_SCRIPT demo.wsgi;
      #工程所在目录
      uwsgi_param UWSGI_CHDIE /opt/app/code6/demo;
      index index.html index.htm;
      client_max_body_size 35M;
    }

}

```

原本项目配置
```
server {
    listen 80;
    server_name localhost;
    charset     utf-8;
    location / {
        try_files $uri @vdidesktop;
    }
    location ^~ /admin{
        alias /opt/www/dist/;
        try_files $uri $uri/   @rewrites;
    }
    location @rewrites {
            rewrite ^/(admin)/(.+)$ /$1/index.html last;
    }
    location @vdidesktop {
      include uwsgi_params;
      #uwsgi_pass unix:/tmp/uwsgi.sock;
      uwsgi_pass localhost:11000;
      rewrite ^/$ /admin redirect;
    }
    client_max_body_size 200M;
}




```
