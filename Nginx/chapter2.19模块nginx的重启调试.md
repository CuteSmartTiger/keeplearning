Nginx模块：

Nginx官方模块

### --with-http_auth_request_module 展示处理Nginx的客户端当前连接或处理的状态

- 此模块配置语法：
```
Syntax：stub_status;

Default:    默认没有

在server下的location位置配置
Context:server,location
```

- 配置如下：
```
location /mystatus {
    stub_status;
    }
```
- 检查与启动
```
nginx -tc /etc/nginx/nginx.conf

nginx -s reload -c /etc/nginx/nginx.conf

nginx -c /etc/nginx/nginx.conf
```

- 访问：
```
http://1.imooc.com/mystatus
```
- 结果：
```
#Nginx当前活跃的连接数
Active connections: 2
#第一个Nginx接受握手的总次数   第二个Nginx处理的连接数，第三个总的请求数
server accepts handled requests
#正常情况下一二相同，表示数据没有丢失
 10 10 7

Reading: 0 Writing: 1 Waiting: 1
```





### --with-http_random_index_module 目录选择一个随机生成主页
- 配置语法：
```
Syntax：random_index on|off;
Default: random_index off;
Context:location
```
cp /opt/backup/default.conf_bak ./default.conf



配置：
vim  /etc/nginx/conf.d/default.conf
```
location / {
        #root   /usr/share/nginx/html;
        root /opt/app/code;
        random_index on;
        #index  index.html index.htm;
```

/opt/app/code 目录下放置了三个文件



- 启动
nginx -tc /etc/nginx/nginx.conf

nginx -s stop -c /etc/nginx/nginx.conf

nginx -c /etc/nginx/nginx.conf


### --with-http_sub_module
语法：替换
```
Syntax：sub_filter string replacement;
Default:
Context:http,server,location
```

语法：检测是否有更新
```
Syntax：sub_filter_last_modified on|off;
Default: sub_filter_last_modified off;
Context:http,server,location
```

语法：是否匹配第一个，可以与替换结合，匹配所有然后进行替换
```
Syntax：sub_filter_once on|off;
Default: sub_filter_once on off;
Context:http,server,location
```


第三方模块
