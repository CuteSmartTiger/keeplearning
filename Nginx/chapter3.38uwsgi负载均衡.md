


GSLB全局负载均衡



SLB  


或者按分层划分：

四层负载均衡



七层负载均衡：针对应用层






通过proxy_pass 模块向upstream server组中的不同服务器转发信息

upstream配置时必须在server层以外，需要在http层


将制定端口的请求信息丢掉：
iptables -I INPUT -p tcp --drop 8002 -j DROP



- 后端负载均衡调度中的状态：

down 当期的server暂时不参与负载均衡
backup 预留的备份服务器
max_fails 允许请求的失败的次数
fail_timeout 经过max_fails 失败后，服务器暂停的时间
max_conns 限制最大接受的连接次数，可以针对不同服务的能力而设定


[Nginx讲解非常好的文章博客](https://blog.csdn.net/zhangskd)
-  调度算法





示例代码：
```
upstream imooc {
  #支持IP 域名 socket的写法
    server 116.62.103.228:8001 down;
    #将现有访问的服务器停掉后重启，backup会上升然后再下降为backup 级别的
    server 116.62.103.228:8002 backup;
    server 116.62.103.228:8003 max_fails=1 fail_timeout=10s;
    }

server {
    listen       80;
    server_name  localhost jeson.t.imooc.io;

    #charset koi8-r;
    access_log  /var/log/nginx/test_proxy.access.log  main;
    resolver  8.8.8.8;

    location / {
      #参数与upstream中的参数名保持一致
        proxy_pass http://imooc;
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
