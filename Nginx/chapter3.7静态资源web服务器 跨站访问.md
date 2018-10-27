静态资源Web服务器的跨站访问：
一般不允许跨站访问，防止CSRF（Cross-site request forgery)攻击


配置语法：
```
#name指head name
Syntax:add_header name value [always];
Default:
Context:http,server,location,if in location


头部信息显示： Access-Control-Allow-Origin
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
         #添加跨域请求，此处是*号，就代表打开所有网站的请求，若有安全需要，则可以将*换为指定可以访问的域名地址
         add_header Access-Control-Allow-Origin *;
         #请求方法
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
