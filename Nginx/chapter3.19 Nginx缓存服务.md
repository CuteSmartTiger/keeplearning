减少后端的压力

客户端缓存：存在浏览器上

服务端缓存：redis  memecached



代理缓存（存在中间件或者代理上）：从服务端获取的备份然后返给客户端使用
代理缓存模式的理解：
缓存服务配置语法：
先定义proxy_cache_path
然后定义proxy_cache


缓存过期周期：
```
#code为返回的状态码，time为设置的过期时间
Syntax:proxy_cache_valid [code] time;
Default:
Context:http,server,location
```


缓存维度
```
Syntax:proxy_cache_key string;
Default:proxy_cache_key $scheme$proxy_host$request_uri;
Context:http,server,location


scheme 代表协议  
proxy_host 主机域名
request_uri 请求地址
```


- 配置示例：

```
upstream imooc {
    server 116.62.103.228:8001;
    server 116.62.103.228:8002;
    server 116.62.103.228:8003;
}
#/opt/app/cache缓存的存储目录
#levels=1:2 目录分为两级
#keys_zone=imooc_cache:10m 开辟的空间名称叫做imooc_cache，大小10m
#max_size=10g 最大存储10g
#inactive=60m 超过60分钟的会被标记，会按照内置规则清理
#use_temp_path=off 减少在cache切换导致的性能损耗
proxy_cache_path /opt/app/cache levels=1:2 keys_zone=imooc_cache:10m max_size=10g inactive=60m use_temp_path=off;

server {
listen       80;
server_name  localhost jeson.t.imooc.io;

#charset koi8-r;
access_log  /var/log/nginx/test_proxy.access.log  main;


location / {
    #上方先定义，若需要开启，则可写成proxy_cache imooc_cache；这里的imooc_cache是在keys_zone=imooc_cache中定义的
    proxy_cache off;
    #代理的方式
    proxy_pass http://imooc;
    #针对返回状态码是200或者304的缓存12小时过期
    proxy_cache_valid 200 304 12h;
    #针对其他返回状态码 10m过期
    proxy_cache_valid any 10m;
    #变量作为缓存的key
    proxy_cache_key $host$uri$is_args$args;
    #增加头信息
    add_header  Nginx-Cache "$upstream_cache_status";  

    #当出现以下错误时调过当前服务器，调到upstream imooc中定义的下一台服务器
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    include proxy_params;
}

#error_page  404              /404.html;

# redirect server error pages to the static page /50x.html
#
error_page   500 502 503 504  /50x.html;
location = /50x.html {
    root   /usr/share/nginx/html;
}

# proxy the PHP scripts to Apache listening on 127.0.0.1:80
#
#location ~ \.php$ {
#    proxy_pass   http://127.0.0.1;
#}

# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#
#location ~ \.php$ {
#    root           html;
#    fastcgi_pass   127.0.0.1:9000;
#    fastcgi_index  index.php;
#    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
#    include        fastcgi_params;
#}

# deny access to .htaccess files, if Apache's document root
# concurs with nginx's one
#
#location ~ /\.ht {
#    deny  all;
#}
}
```

- 如何清理指定缓存
方法一：删除缓存目录
方法二：第三方扩张模块 ngx_cache_purge


- 如何让部分页面不缓存
3-22有介绍
配置语法：
```
Syntax:proxy_no_cache string;
Default:
Context:http,server,location
```


示例
```
if ($request_uri ~ ^/(url3|login|register|password\/reset)) {
  set $cookie_nocache 1;
}

location / {
  proxy_no_cache $cookie_nocache $arg_nocache $arg_comment;
}
```
