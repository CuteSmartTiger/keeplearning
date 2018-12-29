#### 测试脚本
```
#!/bin/bash   
#ip addr | grep 'global eth0' | awk 'BEGIN {count=0;print count} {count=count+1;print $2} END {print count}'


# 获取ip的个数并输出
ip_nums=$(echo ` ip addr | grep 'global eth0' | awk 'BEGIN {count=0;} {count=count+1;} END {print count}'`)
echo ${ip_nums}


if [ "${ip_nums}" == "1" ];
then
    file=/opt/float
    if [ ! -f "$file" ]; then
        touch "$file"  
    fi
    echo 0 > $file

    #value = $(echo ` cat /opt/float`)
    #echo ${value}
    #if [ "${vale}" == "8"];then
    #    echo 'reset tag'
    #    echo 0 > ${file}
    #    exit 0
    #fi

    #监控desktop
    if [ "$(ps -ef | grep "desktop" | grep -v grep)" == "" ]
    then
        echo "died container"
        exit 0
    else
        #杀死desktop容器
        #docker kill vdidesktop-desktop
        echo 'kill container'
        exit 0
    fi
fi

if [ "${ip_nums}" == "2" ]
then
    #判断desktop是否启动
    if [ "$(ps -ef | grep "desktop" | grep -v grep)" == "" ]
    then
        #如果是第一次漂移则启动容器,则设置初始值0，如果不是则返回数字表示容器异常
        file=/opt/float
        if [ ! -f "$file" ]; then
           touch "$file"
           echo 0 > $file
        fi

        #如果file内容为0则代表刚飘逸过来，若为8则表示不是刚飘过来
        value=$(echo ` cat /opt/float`)
        echo ${value}
        if [ "${value}" == "0" ]
        then
            docker start vdidesktop-desktop
            echo 8 > ${file}
            exit 0
        else
            echo "vdidesktop stop" >> /var/log/messages
            exit 4
        fi
    else
        echo 'container alive'
        exit 0
    fi
fi

```

进行调试
bash -x check_vdi



```
n=2
if [ "$n" == "2" ]
then
echo '0'
exit 0
else
echo '4'
exit 4
```

```
value=$(echo `bash /opt/js`)
echo $value

```






#### 第二次调试
```
#!/bin/bash   
#ip addr | grep 'global eth0' | awk 'BEGIN {count=0;print count} {count=count+1;print $2} END {print count}'


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
    fi

    #监控desktop
    if [ "$(ps -ef | grep "desktop" | grep -v grep)" == "" ]
    then
        echo "died container"
        exit 0
    else
        #杀死desktop容器
        docker kill vdidesktop-desktop
        echo 'kill container'
        exit 0
    fi
fi

if [ "${ip_nums}" == "2" ]
then
    #判断desktop是否启动
    if [ "$(ps -ef | grep "desktop" | grep -v grep)" == "" ]
    then
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
            #如果是第一次漂移则启动容器,则设置初始值0，如果不是则返回数字表示容器异常
            file=/opt/float
            if [ ! -f "$file" ]; then
               touch "$file"
               echo 0 > "$file"
            fi

            #如果file内容为0则代表刚飘逸过来
            value=$(echo `cat /opt/float | awk '{print $1 }'`)
            echo ${value}
            if [ "${value}" == 0 ]
            then
                docker start vdidesktop-desktop
                echo 8 > "$file"
                exit 0
            else
                echo "vdidesktop stop" >> /var/log/messages
                exit 4
            fi
        fi
    else
        if [ "$(ps -ef | grep "nginx: master process"| grep -v grep )" == "" ]; then
            echo "nginx stop" >> /var/log/messages
            exit 1

        elif [ "$(ps -ef | grep "salt" | grep -v grep)" == "" ]; then
            echo "salt stop" >> /var/log/messages
            exit 5

        elif [ "$(ps -ef | grep "mysqld" | grep -v grep)" == "" ]; then
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
            echo 'container alive'
            exit 0
        fi
    fi
fi
```



#### 第三版
```
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
    fi

    #监控desktop


    if [ "$(ps -ef | grep "desktop" | grep -v grep)" == "" ]
    then
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
            echo "died container"
            exit 0
        fi
    else
        #杀死desktop容器
        docker kill vdidesktop-desktop
        echo 'kill container'
        exit 0
    fi
fi

if [ "${ip_nums}" == "2" ]
then
    #判断desktop是否启动
    if [ "$(ps -ef | grep "desktop" | grep -v grep)" == "" ]
    then
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
            #如果是第一次漂移则启动容器,则设置初始值0，如果不是则返回数字表示容器异常
            file=/opt/float
            if [ ! -f "$file" ]; then
               touch "$file"
               echo 0 > "$file"
            fi

            #如果file内容为0则代表刚飘逸过来
            value=$(echo `cat /opt/float | awk '{print $1 }'`)
            echo ${value}
            if [ "${value}" == 0 ]
            then
                docker start vdidesktop-desktop
                echo 8 > "$file"
                exit 0
            else
                echo "vdidesktop stop" >> /var/log/messages
                exit 4
            fi
        fi
    else
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
            sleep 40
            if [ "$(ps -ef | grep "nginx: master process"| grep -v grep )" == "" ]; then
                echo "nginx stop" >> /var/log/messages
                exit 1

            elif [ "$(ps -ef | grep "salt" | grep -v grep)" == "" ]; then
                echo "salt stop" >> /var/log/messages
                exit 5
            else
                echo 'container alive'
                exit 0
            fi      
        fi
    fi
fi
```


#### 问题小结
1. 条件判断时注意[ ] 与内外内容之间有空格
2. 引用变量时等号两边没有空格

chmod +x monitor.sh

/etc/init.d/keepalived start

/etc/init.d/keepalived stop
