##### 使用脚本清除日志
vi clean_docker_log.sh
```
#!/bin/sh

logs=`find /var/lib/docker/containers/ -name *-json.log`  

for docker_log in $logs  
do  
echo " "  > $docker_log  
done  
```


##### 使用脚本定时切割日志
```



```



##### 容器自己控制
此方法只针对新创建的容器
```
# vim /etc/docker/daemon.json

{
  "registry-mirrors": ["http://f613ce8f.m.daocloud.io"],
  "log-driver":"json-file",
  "log-opts": {"max-size":"500m", "max-file":"3"}
}
```
