```SHELL
#!/bin/bash
if [ "$(ps -ef | grep vdidesktop | grep -v grep | grep -v  mysql)" == "" ]
then
    echo `date` "vdidesktop stopped" >> /var/log/keepalive.log
    exit 1
else
    if [ "$(ps -ef | grep "mysqld" | grep -v grep)" == "" ]; then
        echo `date` "mysql stopped" >> /var/log/keepalive.log
        exit 2

    elif [ "$(ps -ef | grep "redis"| grep -v grep)" == "" ]; then
        echo `date` "redis stopped" >> /var/log/keepalive.log
        exit 3

    elif [ "$(ps -ef | grep "etcd" | grep -v grep)" == "" ]; then
        echo `date` "etcd stopped" >> /var/log/keepalive.log
        exit 6

    elif [ "$(ps -ef | grep "websock" | grep -v grep)" == "" ]; then
        echo `date` "websocket stopped" >> /var/log/keepalive.log
        exit 7
    else
        if [ "$(ps -ef | grep "nginx: master process"| grep -v grep )" == "" ]; then
            echo `date` "nginx stopped" >> /var/log/keepalive.log
            exit 8

        elif [ "$(ps -ef | grep "salt" | grep -v grep)" == "" ]; then
            echo `date` "salt stopped" >> /var/log/keepalive.log
            exit 5
        else
            echo `date` 'all containers alive' >> /var/log/keepalive.log
            exit 0
        fi
    fi
fi
```
