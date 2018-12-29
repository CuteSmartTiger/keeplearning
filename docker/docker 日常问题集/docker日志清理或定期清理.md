具体的参数，请查看help命令。
docker logs --help

```
docker日志的存储位置：/var/lib/docker/containers/<容器ID>/*.log
```


1. 查看所有容器日志文件大小：
```SHELL
ls -lh $(find /var/lib/docker/containers/ -name *-json.log)
```
2.  临时清理日志文件：
```SHELL
truncate -s 0 /var/lib/docker/containers/<容器ID>/*-json.log

当然也可以这样：
cat /dev/null > *-json.log
注意：rm -rf *-json.log 删除后需要重启容器。如果容器运行的情况下，linux进程会引用着， 不会释放磁盘空间的
```



#### 设置自动清理的脚本
```SHELL
#!/bin/sh

logs=$(find /var/lib/docker/containers/ -name *-json.log)

for log in $logs
    do
        echo "clean logs : $log"
        cat /dev/null > $log
    done
```




#### 日志设置
在dokcer的配置文件中增加日志参数
添加log-dirver和log-opts参数
```
$ vi /etc/docker/daemon.json
"log-driver":"json-file",
"log-opts":{ "max-size" :"50m","max-file":"3"}
#max-file=3，意味着一个容器有三个日志，分别是id+.json、id+1.json、id+2.json




重启生效
sudo systemctl daemon-reload
sudo systemctl restart docker
只针对于新创建的docker有效
```
