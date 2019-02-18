


Nginx
```
nginx -tc /etc/nginx/nginx.conf
nginx -s reload
service nginx restart
```

- Nginx优化时的通用配置
```

user nginx;

# 自己根据服务器检测自动配置
worker_processes auto;
worker_cpu_affinity auto;

error_log /var/log/nginx/error.log warn;

pid /run/nginx.pid;


#调整至1w以上,负荷较高建议2-3w以上
worker_rlimit_nofile 65535;


events {
    # Nginx默认使用而epoll模型
    use epoll;

    # 限制每个进程能处理多少个连接请求,10240x4，
    # 实际最终连接数量有服务器自己的文件句柄最大打开数量决定，ulimit -a 可查看
    worker_connections 10240;
}


http {
    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # 统一使用utf-8字符集
    charset utf-8;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    # Core module
    sendfile            on;

    # 静态资源服务器建议打开
    tcp_nopush          on;

    # 动态资源服务建议打开,需要打开keepalived
    tcp_nodelay         on;
    keepalive_timeout   65;

    # Gzip module
    gzip on;
    gzip_disable "MSIE [1-6]\.";
    gzip_http_version 1.1;

    # Virtal Server
    include /etc/nginx/conf.d/*.conf;
    }
```



##### 参考文章
- [高并发分析与Nginx优化配置](https://www.cnblogs.com/nulige/p/9369700.html)
