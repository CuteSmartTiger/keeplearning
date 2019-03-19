
```shell
#!/bin/bash
log_file=/var/log/keepalive.log

function record_log() {
  #statements
  echo `date "+%Y-%m-%d %H:%M:%S"`  $1 has stopped >> $log_file
  exit $2
}

if [ "$(ps -ef | grep vdidesktop | grep -v grep | grep -v  mysql)" == "" ]
then
    record_log vdidesktop-desktop 1
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
            record_log 'all containers alive,and None' 0
        fi
    fi
fi
```
