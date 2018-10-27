##nginx 日志

error.log
记录错误日志


access.log
http 访问请求相关的记录



tail -f  /var/log/nginx/error.log

tail -n 200 /var/log/nginx/access.log



#### 日志配置：log_format
 vim /etc/nginx/nginx.conf
```
error_log  /var/log/nginx/error.log warn;

#main上下要对应，然后是输出的格式
log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

access_log  /var/log/nginx/access.log  main;
```


nginx 重新加载配置：
nginx -s reload -c /etc/nginx/nginx.conf

#### Nginx变量


HTTP请求变量：
arg_PARAMETER
http_HEADER
sent_http_HEADER


[内置变量](http://nginx.org/en/docs/)

自定义变量：

查看进程
ps -aux|grep nginx
