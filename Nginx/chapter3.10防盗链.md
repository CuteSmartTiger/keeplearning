http_refer 防盗链配置（有局限性）
作用：防止爬虫 盗取资料等信息
配置语法：
```
Syntax:valid_referers none|blocked|server_name|string;
Default:
Context:server,location
```


示例：
```
location ~ .*\.(jpg|gif|png)$ {
    gzip on;
    gzip_http_version 1.1;
    gzip_comp_level 2;
    gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript application/x-httpd-php image/jpeg image/gif image/png;

    #valid_referers表示允许的连接，none表示允许没有带refer信息的通过，blocked表示允许非正式的请求或不带协议的请求，
    #若只有116.62.103.228，则代表只允许此ip访问
    valid_referers none blocked 116.62.103.228 jeson.imoocc.com ~wei\.png;
    #若invalid_referer变量为空时，则返回403错误
    if ($invalid_referer) {
        return 403;
    }
```



其他知识补充：
只获取访问的头部信息
curl -I www.baidu.com


从谷歌refer信息发送
curl -e "http://google.com" -I www.baidu.com
