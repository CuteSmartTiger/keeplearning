redis的启动方式
1.直接启动
  进入redis根目录，执行命令:
  #加上‘&’号使redis以后台程序方式运行
```
./redis-server &
```

2.通过指定配置文件启动
可以为redis服务启动指定配置文件，例如配置为/etc/redis/6379.conf
进入redis根目录，输入命令：
```
./redis-server /etc/redis/6379.conf
```
如果更改了端口，使用`redis-cli`客户端连接时，也需要指定端口，例如：
```
redis-cli -p 6380
```
3.使用redis启动脚本设置开机自启动
见网页：https://www.cnblogs.com/pqchao/p/6549510.html
