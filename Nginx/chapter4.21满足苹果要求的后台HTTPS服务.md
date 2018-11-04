

```
server
 {
   listen       443;
   server_name  116.62.103.228 jeson.t.imooc.io;
   #保持的连接时间
   keepalive_timeout 100;

   ssl on;
   #共享缓存，配置10M
   ssl_session_cache   shared:SSL:10m;
   #过期时间10分钟
   ssl_session_timeout 10m;

   #ssl_certificate /etc/nginx/ssl_key/jesonc.crt;
   ssl_certificate /etc/nginx/ssl_key/jesonc_apple.crt;
   ssl_certificate_key /etc/nginx/ssl_key/jesonc.key;
   #ssl_certificate_key /etc/nginx/ssl_key/jesonc_nopass.key;

   index index.html index.htm;
   location / {
       root  /opt/app/code;
   }
}



```


HTTPS服务优化：
方法一：激活keepalive长连接
方法二：设置ssl session缓存
