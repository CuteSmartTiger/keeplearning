## rewrite规则

### 使用场景
- 1.URL访问跳转 支持开发设计
页面跳转 兼容性支持  展示效果等


- 2.SEO的优化
符合google或者百度的搜索



- 3.维护
后台维护，流量转发等


- 4.安全
实现伪静态，让真实的动态页面进行伪装


### rewrite配置语法
```
Syntax:rewrite regex replacement [flag];
Default:
Context:server,location,if

#示例：
#匹配方法   指定到对应的目录下的文件   
rewrite ^(.*)$ /pages/maintain.html break;
```

### 正则表达式
常用，可以网上看详细的

| 符号 | 含义 |
| --- | --- |
| .  | 除了换行以外的任意字符|
|?   |重复0或者1次
|+   |重复1次或者更多次
|*   |
|\d | 匹配数字
|^|
|$|



### pcre验证正则表达式的工具
pcre
pcretest


### flag
last
break
redirect  返回302，临时重定向
permanent  返回301，永久重定向


last与break示例与解说：
```
server {
    listen 80 default_server;
    server_name jeson.t.imooc.io;

    access_log  /var/log/nginx/log/host.access.log  main;

    #flag为break，在匹配访问break时，会跳转访问 /opt/app/code目录下的test目录，若目录不存在，则返回Nginx对应的错误
    root /opt/app/code;
    location ~ ^/break {
        rewrite ^/break /test/ break;
    }

    #flag为break，在匹配访问last路径时，会跳转访问 /opt/app/code目录下的test目录，若目录不存在，则建立新的连接，跳转到下一个location
    location ~ ^/last {
         rewrite ^/last /test/ last;
    }    

    location /test/ {
       #设置默认格式
       default_type application/json;
      #返回的状态码与信息
       return 200 '{"status":"success"}';
    }
}

```

redirect与permanent示例与解说
```
server {
    listen 80 default_server;
    server_name jeson.t.imooc.io;

    access_log  /var/log/nginx/log/host.access.log  main;

    root /opt/app/code;
    location ~ ^/break {
        rewrite ^/break /test/ break;
    }

    location ~ ^/last {
         rewrite ^/last /test/ last;
         #rewrite ^/last /test/ redirect;
    }    

    location ~ ^/imooc {
         #永久重定向，第一次访问跳转后，在把Nginx服务关闭，依然可以访问，服务器会记录重定向的地址
         rewrite ^/imooc http://www.imooc.com/ permanent;
         #临时重定向，当把Nginx服务关闭时，再次访问时依然需要重定向，而且此时访问会失败
         #rewrite ^/imooc http://www.imooc.com/ redirect;
    }    

    location /test/ {
       default_type application/json;
       return 200 '{"status":"success"}';
    }
}
```


示例三：
```
server {
    listen       80;
    server_name  localhost;

    #charset koi8-r;
    #access_log  /var/log/nginx/log/host.access.log  main;
    root   /opt/app/code;

    location / {
        #$1 $2 $3 三个对应前面的三个参数
        rewrite ^/course-(\d+)-(\d+)-(\d+)\.html$ /course/$1/$2/course_$3.html break;

        #匹配使用Chrome浏览器打开
        if ($http_user_agent ~* Chrome) {
            rewrite ^/nginx http://coding.imooc.com/class/121.html redirect;
        }

        #匹配不满足文件路径名的重定向
        if (!-f $request_filename) {
            rewrite ^/(.*)$ http://www.baidu.com/$1 redirect;
        }
        index  index.html index.htm;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504 404  /50x.html;
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


相关命令：
查看请求得过程
curl -vL jeson.t.imooc.io/last



### rewrite规则优先级
先执行，server块的rewrite指令
再执行，location匹配
然后，执行选定的location中的rewrite
