静态资源类型：
浏览器端的渲染  HTML CSS JS
图片   JEPG GIF PNG
视频   FLV MPEG
文件   TXT 等任意下载文件


文件读取
```
Syntax:sendfile on|off;
Default:sendfile off;
Context:http,server,if in location

```


提高文件传输效率,将多个包整合后再发送，大文件比较推荐
- tcp_nopush
```
Syntax:tcp_nopush on|off;
Default:tcp_nopush off;
Context:http,server,location
```

- tcp_nodelay
作用：keepalive强连接下，提高网络包的传输实时性
```
Syntax:tcp_nodelay on|off;
Default:tcp_nodelay on;
Context:http,server,location
```

- 压缩：
作用：压缩传输,对文本压缩效果比较明显
```
Syntax:gzip on|off;
Default:gzip off;
Context:http,server,location,if in location
```

作用：压缩比
```
Syntax:gzip_comp_level level;
Default:gzip_comp_level 1;
Context:http,server,location
```

压缩协议版本：
```
Syntax:gzip_http_version 1.0|1.1;
Default:gzip_http_version 1.1;
Context:http,server,location
```


- 配置示例：
```
server {
    listen       80;
    server_name  116.62.103.228 jeson.imooc.com;

    sendfile on;
    #charset koi8-r;
    access_log  /var/log/nginx/log/static_access.log  main;

    #匹配图片格式
    location ~ .*\.(jpg|gif|png)$ {
        gzip on;
        gzip_http_version 1.1;
        gzip_comp_level 2;
        gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript application/x-httpd-php image/jpeg image/gif image/png;
        root  /opt/app/code/images;
    }
    #匹配文本或者xml
    location ~ .*\.(txt|xml)$ {
        gzip on;
        gzip_http_version 1.1;
        gzip_comp_level 1;
        gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript application/x-httpd-php image/jpeg image/gif image/png;
        root  /opt/app/code/doc;
    }
    #匹配以download开始的url
    location ~ ^/download {
      #需要预先压缩
        gzip_static on;
        tcp_nopush on;
        root /opt/app/code;
    }
```
