
```shell
#!/bin/bash

# 定义日志存储的文件
log_file=/var/log/keepalive.log

function record_log() {
  #记录日志
  echo `date "+%Y-%m-%d %H:%M:%S"`  $1 has stopped >> $log_file
  exit $2
}


# 检查虚拟ip是否存在，不存在则重启keepalived服务
function check_virtual_ip() {
vir_ip=$(echo `egrep '([0-9]{1,3}\.){1,3}[0-9]{1,3}' /etc/keepalived/keepalived.conf | awk '{ print $1 }'`)

ping_ip=$(echo `ping -c 1  ${vir_ip} | grep "packet loss" | awk '{ print $4 }'`)

if [ "${ping_ip}"x == "0"x ];then
  `service keepalived restart`
  exit 1
else
  exit 0
fi
}


if [ "$(ps -ef | grep vdidesktop | grep -v grep | grep -v  mysql)" == "" ]
then
    `record_log vdidesktop-desktop 1`
else
    if [ "$(ps -ef | grep "mysqld" | grep -v grep)" == "" ]; then
        record_log vdidesktop-mysql 2
    elif [ "$(ps -ef | grep "redis"| grep -v grep)" == "" ]; then
        record_log vdidesktop-redis 3
    elif [ "$(ps -ef | grep "etcd" | grep -v grep)" == "" ]; then
        record_log vdidesktop-etcd 4
    elif [ "$(ps -ef | grep "websock" | grep -v grep)" == "" ]; then
        record_log vdidesktop-websock 5
    else
        if [ "$(ps -ef | grep "nginx: master process"| grep -v grep )" == "" ]; then
            record_log 'nginx:master process' 6
        elif [ "$(ps -ef | grep "salt" | grep -v grep)" == "" ]; then
            record_log salt 7
        else
          check_virtual_ip
          if [ "$?" == "0" ];then
            record_log 'all containers alive,and None' 0
          else
            record_log 'all containers alive,but keepalived' 0
          fi
        fi
    fi
fi
```
