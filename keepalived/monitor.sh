#!/bin/bash

# 获取ip的个数并输出
ip_nums=$(echo ` ip addr | grep 'global eth0' | awk 'BEGIN {count=0;} {count=count+1;} END {print count}'`)
echo ${ip_nums}


if [ "${ip_nums}" == "1" ];
then
    file=/opt/float
    if [ ! -f "$file" ]; then
        touch "$file"
        echo 0 > "$file"
    fi

    value=$(echo `cat /opt/float`)
    echo ${value}
    if [ "${value}" == "8" ];then
        echo 'reset tag'
        echo 0 > ${file}
        echo `date` "use 0 to replace 8 in /opt/float" >> /var/log/messages
    fi

    #监控desktop


    if [ "$(ps -ef | grep vdidesktop | grep -v grep | grep -v  mysql)" == "" ]
    then
        if [ "$(ps -ef | grep "mysqld" | grep -v grep)" == "" ]; then
            echo `date`  "mysql stop" >> /var/log/messages
            exit 2

        elif [ "$(ps -ef | grep "redis"| grep -v grep)" == "" ]; then
            echo `date`   "redis stop" >> /var/log/messages
            exit 3

        elif [ "$(ps -ef | grep "etcd" | grep -v grep)" == "" ]; then
            echo `date` "etcd stop" >> /var/log/messages
            exit 6

        elif [ "$(ps -ef | grep "websock" | grep -v grep)" == "" ]; then
            echo `date` "websocket stop" >> /var/log/messages
            exit 7
        else
            echo `date` "died container" >> /var/log/messages
            exit 0
        fi
    else
        #杀死desktop容器
        docker kill vdidesktop-desktop
        echo `date` 'kill container' >> /var/log/messages
        exit 0
    fi
fi


if [ "${ip_nums}" == "2" ]
then
    #判断desktop是否启动
    if [ "$(ps -ef | grep vdidesktop | grep -v grep | grep -v  mysql)" == "" ]
    then
        if [ "$(ps -ef | grep "mysqld" | grep -v grep)" == "" ]; then
            echo `date` "mysql stop" >> /var/log/messages
            exit 2

        elif [ "$(ps -ef | grep "redis"| grep -v grep)" == "" ]; then
            echo `date` "redis stop" >> /var/log/messages
            exit 3

        elif [ "$(ps -ef | grep "etcd" | grep -v grep)" == "" ]; then
            echo `date` "etcd stop" >> /var/log/messages
            exit 6

        elif [ "$(ps -ef | grep "websock" | grep -v grep)" == "" ]; then
            echo `date` "etcd stop" >> /var/log/messages
            exit 7
        else
            #如果是第一次漂移则启动容器,则设置初始值0，如果不是则返回数字表示容器异常
            file=/opt/float
            if [ ! -f "$file" ]; then
               touch "$file"
               echo 0 > "$file"
               echo `date` 'there is no /opt/float ,and created it ,then mark 0'
            fi

            #如果file内容为0则代表刚飘逸过来
            value=$(echo `cat /opt/float | awk '{print $1 }'`)
            echo ${value}
            if [ "${value}" == 0 ]
            then
                docker start vdidesktop-desktop
                echo 8 > "$file"
                echo `date` "docker start vdidesktop  and set 8 in /opt/file" >> /var/log/messages
                exit 0
            else
                echo `date` "vdidesktop stop" >> /var/log/messages
                exit 4
            fi
        fi
    else
        if [ "$(ps -ef | grep "mysqld" | grep -v grep)" == "" ]; then
            echo `date` "mysql stop" >> /var/log/messages
            exit 2

        elif [ "$(ps -ef | grep "redis"| grep -v grep)" == "" ]; then
            echo `date` "redis stop" >> /var/log/messages
            exit 3

        elif [ "$(ps -ef | grep "etcd" | grep -v grep)" == "" ]; then
            echo `date` "etcd stop" >> /var/log/messages
            exit 6

        elif [ "$(ps -ef | grep "websock" | grep -v grep)" == "" ]; then
            echo `date` "websocket stop" >> /var/log/messages
            exit 7
        else
            sleep 40
            if [ "$(ps -ef | grep "nginx: master process"| grep -v grep )" == "" ]; then
                echo `date` "nginx stop" >> /var/log/messages
                exit 1

            elif [ "$(ps -ef | grep "salt" | grep -v grep)" == "" ]; then
                echo `date` "salt stop" >> /var/log/messages
                exit 5
            else
                echo `date` 'container alive' >> /var/log/messages
                exit 0
            fi
        fi
    fi
fi
