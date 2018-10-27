连接频率限制
limit_conn_module


请求频率限制
limit_req_module




http1.1  顺序性TCP复用

http2.0   多路复用TCP复用




语法：
```
Syntax:limit_conn_zone key zone=name:size;
Default:
Context:http


允许同一时间连接的数量，要先配置好上面的才可以配置下面的
Syntax：limit_conn zone number;
Default:
Context:http,server,location
```
