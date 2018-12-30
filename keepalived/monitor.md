#### 第一版
```
if [ "$(ps -ef | grep "nginx: master process"| grep -v grep )" == "" ]; then
    # 输出日志
    echo "nginx stop" >> /var/log/messages
    exit 1
elif [ "$(ps -ef | grep "redis"| grep -v grep)" == "" ]; then
    echo "redis stop" >> /var/log/messages
    exit 2

elif [ "$(ps -ef | grep "mysqld" | grep -v grep)" == "" ]; then
    echo "mysql stop" >> /var/log/messages
    exit 3

#elif [ "$(ps -ef | grep "desktop" | grep -v grep)" == "" ]; then
    #echo "vdidesktop stop" >> /var/log/messages
    #exit 4
elif [ "$(ps -ef | grep "salt" | grep -v grep)" == "" ]; then
    echo "salt stop" >> /var/log/messages
    exit 5
elif [ "$(ps -ef | grep "etcd" | grep -v grep)" == "" ]; then
    echo "etcd stop" >> /var/log/messages
    exit 6
elif [ "$(ps -ef | grep "websock" | grep -v grep)" == "" ]; then
    echo "etcd stop" >> /var/log/messages
    exit 7
else
    # 一切正常
    value=$(echo `bash /opt/check_vdi`)
    if [ "${value}" == "4" ];then
        exit 4
    else
	     exit 0
    fi
fi
```

#### 第二版
把与vdidesttop相关的进程监控放在容器监控的后面
```
#!/bin/bash  
if [ "$(ps -ef | grep "mysqld" | grep -v grep)" == "" ]; then
    echo "mysql stop" >> /var/log/messages
    exit 2    

elif [ "$(ps -ef | grep "redis"| grep -v grep)" == "" ]; then
    echo "redis stop" >> /var/log/messages
    exit 3

elif [ "$(ps -ef | grep "etcd" | grep -v grep)" == "" ]; then
    echo "etcd stop" >> /var/log/messages
    exit 6

elif [ "$(ps -ef | grep "websock" | grep -v grep)" == "" ]; then
    echo "etcd stop" >> /var/log/messages
    exit 7

else
    # 一切正常
    #value=$(echo `bash /opt/check_vdi`)
    bash /opt/check_vdi
    value=$?

    if [ "${value}" == "4" ];then
        echo "vdidesktop stop" >> /var/log/messages
        exit 4
    else
        if [ "$(ps -ef | grep "nginx: master process"| grep -v grep )" == "" ]; then
            # 输出日志
            echo "nginx stop" >> /var/log/messages
            exit 1

        elif [ "$(ps -ef | grep "salt" | grep -v grep)" == "" ]; then
            echo "salt stop" >> /var/log/messages
            exit 5
        else  
    	     exit 0
        fi
    fi
fi


```
