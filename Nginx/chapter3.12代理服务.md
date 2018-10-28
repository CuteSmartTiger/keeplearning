代理的作用：


正向代理
为客户端服务

反向代理：
为服务端服务


Nginx支持的协议有：
HTTP
Websocket
GRPC  远程调用go语言的协议
ICMP\POP\IMAP\HTTPS   
RTMP                   针对视频



反向代理与Nginx模块
http websocket https    ngx_http_proxy_module
fastcgi    ngx_http_fastcgi_module
uwsgi      ngx_http_uwsgi_module
grcp      ngx_http_v2_module


反向代理配置语法：
配置语法：
```
#URL为代理访问的url地址
Syntax:proxy_pass URL;
Default:
Context:location，if in location,limit_except
```

配置示例：
```
server {
    listen       80;
    server_name  localhost jeson.t.imooc.io;

    #charset koi8-r;
    access_log  /var/log/nginx/test_proxy.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    #通过公网访问80端口，然后反向代理访问本机8080端口
    #location ~ /test_proxy.html$ {
    #    proxy_pass http://127.0.0.1:8080;
    #}
```

此处疑问：为什么公网可以访问80端口，而不可以通过8080端口访问


正向代理与Nginx模块（比较不常用,而且不支持HTTPS协议）
HTTP    ngx_http_proxy_module

配置示例：
```
location / {
  #匹配非目标ip则返回403
    if ( $http_x_forwarded_for !~* "^116\.62\.103\.228") {
        return 403;
    }
    root   /opt/app/code;
    index  index.html index.htm;
}
```


配置示例2：
```
listen       80;
server_name  localhost jeson.t.imooc.io;

#charset koi8-r;
access_log  /var/log/nginx/test_proxy.access.log  main;
resolver 8.8.8.8;
location / {  
    proxy_pass http://$http_host$request_uri;
}  
```



跳转重定向

头信息

超时


配置示例：
```
location / {
  proxy_pass http://127.0.0.1:8080;
  #跳转重定向
  proxy_redirect defautl;

  #头信息
  proxy_set_header Host &http_host;
  proxy_set_header X-Real-IP $remote_addr;

  #超时
  proxy_connect_timeout 30;
  proxy_send_time 60;
  proxy_read_time 60;

  #缓冲
  proxy_buffer_size 32k;
  proxy_buffering on;
  proxy_buffers 4 128k;
  proxy_bbusy_buffers_size 256k;
  proxy_max_temp_file_size 256k;
}
```
