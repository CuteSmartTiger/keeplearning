### 基于host域名的虚拟机配置方式（http协议）
之前两种则为tcp协议


配置客户端即DNS域名解析：
Linux下：
vim /etc/hosts

Windows下：C:\Windows\System32\drivers\etc
192.168.6.90 1.imooc.com
192.168.6.90 2.imooc.com

192.168.6.90 liuhu1.test.com
192.168.6.90 liuhu2.test.com



检查是否成功
ping 1.imooc.com
ping 2.imooc.com

ping liuhu1.test.com
ping liuhu2.test.com


netstat -ntpl


vi /etc/nginx/conf.d/vserver1.conf
```
#server_name  localhost;
     server_name  liuhu1.test.com;
```


nginx -tc /etc/nginx/nginx.conf

nginx -s stop -c /etc/nginx/nginx.conf

nginx -c /etc/nginx/nginx.conf

iptables -F

http://liuhu1.test.com/server.html

1.imooc.com/server.html


关闭：
kill -9 PID号


可以通过以下调试访问：
curl 1.imooc.com/server.html
curl 2.imooc.com/server.html
