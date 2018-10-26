### 基于host域名的虚拟机配置方式（http协议）
之前两种则为tcp协议



配置宿主的即DNS域名解析：
vim /etc/hosts
192.168.6.90 liuhu1.test.com
192.168.6.90 liuhu2.test.com

检查是否成功
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


关闭：
kill -9 PID号
