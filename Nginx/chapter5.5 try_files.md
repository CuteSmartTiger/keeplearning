```
server {
    listen       80;
    server_name  testserver1 jeson.t.imoocc.io;

    #charset koi8-r;
    #access_log  /var/log/nginx/log/host.access.log  main;
    #root   /opt/app;

    #location ^~ /code {
    #    rewrite ^(.*)$ /code2/index.html break;
    #}
    #location ~ /code.* {
    #    rewrite ^(.*)$ /code3/index.html break;
    #}
    #location = /code1 {
    #    rewrite ^(.*)$ /code1/index.html break;
    #}


    location / {
        root /opt/app/code/cache;
        #首先查找cache目录下的URI，若不存在，则查找@java_page，下一个location处
        try_files $uri @java_page;
    }

    #定义@java_page的代理地址
    location @java_page{
        proxy_pass http://127.0.0.1:9090;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504 404  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}


```
