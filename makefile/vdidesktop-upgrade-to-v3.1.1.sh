#!/bin/bash

# 日志配置文件复制
cp -f logrotate.conf /etc/
cp -rf logconf/. /etc/logrotate.d/
service cron reload
service cron restart

# install keepalive
dpkg -i debs/*.deb
cp -f conf/monitor.sh /etc/keepalived/
sudo chmod  a+x /etc/keepalived/monitor.sh
cp -f conf/keepalived.conf /etc/keepalived/
cp -f conf/rc.local /etc/rc.local
chmod a+x /etc/rc.local

# 加载镜像
docker load -i vdidesktop-desktop-3.1.1.0115.docker
docker load -i etcd-3.1.1.docker
docker load -i novnc-websocket-3.docker


# 针对数据库


mysql_map=$( echo `docker ps -a | grep mysql | grep '0.0.0.0:3306->3306/tcp'`)

if [ "${mysql_map}"T = ""T ];
then
    is_mysql_exist=$(echo `docker ps -a | grep mysql`)
    if [ "${is_mysql_exist}"s = ""s ];
    then
        echo 'there is no mysql contaniner'
    else
        docker kill vdidesktop-mysql
        docker rm vdidesktop-mysql
        sleep 1
        echo 'rm mysql contaniner'
    fi
else
    echo 'mysql port has mapped, it is OK'
fi


#!/bin/bash
redis_log_file='/var/log/redis'
if [ ! -d "${redis_log_file}" ]; then
  is_redis_exist=$(echo `docker ps -a | grep vdidesktop-redis`)
  if [ "${is_redis_exist}s" = "s" ];
  then
      echo 'there is no redis contaniner'
  else
      docker kill vdidesktop-redis
      docker rm vdidesktop-redis
      sleep 1
      echo 'rm redis contaniner'
  fi
else
  echo 'redis log directory has mapped, it is OK'
fi




mv /opt/docker/Makefile /opt/docker/Makefile.bak
cp Makefile.for_customer /opt/docker/Makefile
cd /opt/docker
make rm-only
docker tag 192.168.5.8:5001/vdidesktop-desktop:active 192.168.5.8:5001/vdidesktop-desktop:old
docker tag 192.168.5.8:5001/vdidesktop-desktop:latest 192.168.5.8:5001/vdidesktop-desktop:active
make run

cd -
