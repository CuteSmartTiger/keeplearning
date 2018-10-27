静态资源浏览器的缓存：

HTTP协议定义的缓存

浏览器无缓存

客户端有缓存

- 检验机制
检验是否过期              Cache-Control(max-age)      
协议中Etag头信息校验       Etag
Last-Modified头信息校验   Last-Modified


配置语法：
```
Syntax:expires [Modified] time;
       expires epoch |max|off;
Default:expires off;
Context:http,server,location,if in location

```


 设置过期时间配置：
 ```
 server {
     listen       80;
     server_name  116.62.103.228 jeson.imoocc.com www.jesonc.com;

     sendfile on;
     #charset koi8-r;
     access_log  /var/log/nginx/log/static_access.log  main;


     location ~ .*\.(jpg|gif|png)$ {
         gzip on;
         gzip_http_version 1.1;
         gzip_comp_level 2;
         gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript application/x-httpd-php image/jpeg image/gif image/png;
         root  /opt/app/code/images;
     }

     location ~ .*\.(txt|xml)$ {
         gzip on;
         gzip_http_version 1.1;
         gzip_comp_level 1;
         gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript application/x-httpd-php image/jpeg image/gif image/png;
         root  /opt/app/code/doc;
     }

     location ~ .*\.(htm|html)$ {
         add_header Access-Control-Allow-Origin *;
         add_header Access-Control-Allow-Methods GET,POST,PUT,DELETE,OPTIONS;
         #设置过期时间
         #expires 24h;
         root  /opt/app/code;
     }

     location ~ ^/download {
         gzip_static on;
         tcp_nopush on;
         root /opt/app/code;
     }
 ```
