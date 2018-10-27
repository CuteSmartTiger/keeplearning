请求限制语法：
```
Syntax:limit_req_zone key zone=name:size rate=rate;
Default:
Context:http


允许同一时间连接的数量，要先配置好上面的才可以配置下面的
Syntax：limit_req zone=name [number] [nodelay];
Default:
Context:http,server,location
```


压力测试语法：n代表请求数，c表示并发数
ab -n 100 -c 10 http://www.baidu.com/

配置：
```
limit_conn_zone $binary_remote_addr zone=conn_zone:1m;
limit_req_zone $binary_remote_addr zone=req_zone:1m rate=1r/s;
server {
listen       80;
server_name  localhost;

#charset koi8-r;
#access_log  /var/log/nginx/log/host.access.log  main;


location / {
    root /opt/app/code;
    limit_conn conn_zone 1;
    #limit_req zone=req_zone burst=3 nodelay;
    #limit_req zone=req_zone burst=3;
    #limit_req zone=req_zone;
    index  index.html index.htm;
}
```
