### Nginx 默认配置语法
vi /etc/nginx/nginx.conf
```
#设置Nginx服务的系统使用用户
user  nginx;

#工作进程数，与CPU核心数保持一致即可
worker_processes  1;

#Nginx错误日志
error_log  /var/log/nginx/error.log warn;

#Nginx服务启动时的pid
pid        /var/run/nginx.pid;

#两个参数：
#其一为：worker_connections，每个进程允许的最大连接数
#其二为：use，工作进程数
events {
    worker_connections  1024;
}


#自己配置的参数
http {
  …… ……
  server {
    #监听端口
    listen          80;
    #服务器名称，可以是域名，也可以是服务器ip地址
    server_name     localhost;

    #访问首页时浏览的文件位置，控制访问首页
    location / {
      root /usr/share/nginx/html;
      index index.html index.htm;
    }

    #错误代码时访问的统一页面
    error_page 500 502 503 504 /50x.html;
    location = /50x.html{
      root /usr/share/nginx/html;
    }
  }

  #下一个服务器的配置
  server {
    …… ……
  }

}


#虚拟机自带的配置
http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}

```
