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
            vir_ip=$(echo `egrep '([0-9]{1,3}\.){1,3}[0-9]{1,3}' /etc/keepalived/keepalived.conf | awk '{ print $1 }'`)
            echo `date` "there defined virtual ip is ${vir_ip}" >> /var/log/keepalive.log

            ping_ip=$(echo `ping -c 1  ${vir_ip} | grep "packet loss" | awk '{ print $4 }'`)

            if [ "${ping_ip}" == "0" ];then

              `service keepalived restart`

              echo `date` "there is no virtual ip,then restart keepalived" >> /var/log/keepalive.log
            else
              echo `date` 'all containers alive,and virtual ip exists' >> /var/log/keepalive.log

              exit 0
            fi
        fi
    fi
fi
