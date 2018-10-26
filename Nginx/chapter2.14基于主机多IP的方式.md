### 基于主机多IP的方式

#### 多网卡IP的方式




#### 单网卡多IP的方式
注：阿里云不适合

- 查看ip命令
```
ip -a
或
ifconfig
```
解释：
lo   eth0   docker0的含义

- 添加网卡ip地址
ip a add 192.168.6.95/24 dev eth0


- 配置default.conf
cd /etc/nginx/conf.d/


先备份(针对修改会出问题的文件可以进行如此操作)
cp default.conf /opt/backup/default.conf_bak

给默认文件改名字
 mv default.conf vserver1.conf

复制产生第二个配置文件：
cp vserver1.conf vserver2.conf

分别配置IP


停止Nginx服务：
nginx -s stop -c /etc/nginx/nginx.conf

启动服务：
nginx -c /etc/nginx/nginx.conf


vi /etc/nginx/conf.d/vserver1.conf
vserver1.conf
```
erver {
    listen      192.168.6.90:80;
    server_name  localhost;

    #charset koi8-r;
    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        #root   /usr/share/nginx/html;
        root   /opt/app/code;
        index  index.html index.htm;
```



vi /etc/nginx/conf.d/vserver2.conf
```
server {
    listen  192.168.6.95:80;
    server_name  localhost;

    #charset koi8-r;
    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        #root   /usr/share/nginx/html;
        root   /opt/app/code1;
}
```
