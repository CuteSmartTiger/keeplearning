
```
nginx 负载均衡5种配置方式

1、轮询（默认）   

每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除。  

2、weight
指定轮询几率，weight和访问比率成正比，用于后端服务器性能不均的情况。  权重越高  访问次数越多
例如：  
upstream bakend {  
server 192.168.0.14 weight=10;  
server 192.168.0.15 weight=15;  
}  

3、ip_hash
每个请求按访问ip的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session或者cookie的问题。存在缺点
例如：  
upstream bakend {  
ip_hash;  
server 192.168.0.14:88;  
server 192.168.0.15:80;  
}  

4、fair（第三方）   
按后端服务器的响应时间来分配请求，响应时间短的优先分配。  
upstream backend {  
server server1;  
server server2;  
fair;  
}  


#1.72版本以后
5、url_hash（第三方）   

按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效。  

例：在upstream中加入hash语句，server语句中不能写入weight等其他的参数，hash_method是使用的hash算法  

upstream backend {  
server squid1:3128;  
server squid2:3128;  
#request_uri是指请求参数，相同的URI，会访问相同的服务器，这样多次访问 缓存等信息保持一致
hash $request_uri;  
hash_method crc32;  
}  



tips:  

upstream bakend{#定义负载均衡设备的Ip及设备状态  
ip_hash;  
server 127.0.0.1:9090 down;  
server 127.0.0.1:8080 weight=2;  
server 127.0.0.1:6060;  
server 127.0.0.1:7070 backup;  
}  
在需要使用负载均衡的server中增加  
proxy_pass http://bakend/;  
```
