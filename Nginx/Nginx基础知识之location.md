### 语法规则：
- 1、“=” 开头表示精确匹配

- 2、“^~” 开头表示uri以某个常规字符串开头，理解为匹配url路径即可。nginx不对url做编码，因此请求为/static/20%/aa，可以被规则^~ /static/ /aa匹配到（注意是空格）。

- 3、“~” 开头表示区分大小写的正则匹配

- 4、“~*” 开头表示不区分大小写的正则匹配

- 5、“!~”和“!~*”分别为区分大小写不匹配及不区分大小写不匹配 的正则

- 6、“/” 通用匹配，任何请求都会匹配到


### http下的一些配置及其意义
```
include       mime.types; #文件扩展名与文件类型映射表
default_type  application/octet-stream; #默认文件类型
sendfile on;  #开启高效文件传输模式，sendfile指令指定nginx是否调用sendfile函数来 输出文件，对于普通应用设为 on，如果用来进行下载等应用磁盘IO重负载应用，可设置 为off，以平衡磁盘与网络I/O处理速度，降低系统的负载。注意:如果图片显示不正常 把这个改成off。
autoindex on; #开启目录列表访问，合适下载服务器，默认关闭。
tcp_nopush on; #防止网络阻塞
tcp_nodelay on; #防止网络阻塞
keepalive_timeout 120; #长连接超时时间，单位是秒
gzip on; #开启gzip压缩输出
```


### server虚拟主机一些配置及其意义
```
http{
 #虚拟主机1
 server{
  listen       80;
  server_name  www.nginx1.com;
  location / {
     root   html;
     index  index.html index.htm;
  }
 }

 #虚拟主机2
 server{
  listen       80;
  server_name  localhost;
  location / {
     root   html;
     index  index.html index.htm;
  }
 }
}
```

补充说明：这里server_name配置域名的时候，如果是本地测试，需要到windos下hosts文件里，把你的域名和ip添加进去（C:\Windows\System32\drivers\etc\hosts）


### nginx支持三种类型的 虚拟主机配置

- 1、基于ip的虚拟主机， (一块主机绑定多个ip地址)
```
server{
  listen       192.168.1.1:80;
  server_name  localhost;
}
server{
  listen       192.168.1.2:80;
  server_name  localhost;
}
```

- 2、基于域名的虚拟主机(servername)
```
#域名可以有多个，用空格隔开
server{
  listen       80;
  server_name  www.nginx1.com www.nginx2.com;
}
server{
  listen       80;
  server_name  www.nginx3.com;
}
```

- 3、基于端口的虚拟主机(listen不写ip的端口模式)
```
server{
  listen       80;
  server_name  localhost;
}
server{
  listen       81;
  server_name  localhost;
}
```


### 参考文献：
[nginx.conf配置文件解析(http、server、location)](https://blog.csdn.net/chenweijiSun/article/details/70823482)
