方法一：通过设置response的头信息Nginx-Cache
通过response让客户端获取状态信息
add_header Nginx-Cache "$upstream_cache_status";


upstream_cache_status状态类型
MISS
HIT
EXPIRED
UPDATING
STALE


配置示例：
```
location / {
    proxy_cache imooc_cache;
    proxy_pass http://imooc;
    proxy_cache_valid 200 304 12h;
    proxy_cache_valid any 10m;
    proxy_cache_key $host$uri$is_args$args;
    # Nginx-Cache为变量，可以自定义
    add_header  Nginx-Cache $upstream_cache_status;  

    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    include proxy_params;
}
```


###  打印日志分析统计下缓存命中率
缓存命中率 = HIT次数 / 总请求次数
实现方式：分析Nginx里的access日志

awk 命令

在/etc/nginx/nginx.conf配置log_format
```

er  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"'
                      #此处必须要使用单引号再用双引号，前面使用空格以便后续使用awk工具分析日志
                      ' "$upstream_cache_status"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}

```

# $NF表示取每行末尾的匹配值,结束后格式化打印，hit总数除以NR总的请求数
```
awk '{if($NF=="\"HIT\""){hit++}}END{printf"%.2f",hit/NR}' /var/log/nginx/access.log
```

日志清空的快速方法：
```
 > /var/log/nginx/access.log
```
