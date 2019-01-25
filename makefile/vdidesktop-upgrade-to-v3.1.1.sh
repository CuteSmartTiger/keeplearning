#!/bin/bash

# 日志配置文件复制
cp -f logrotate.conf /etc/
cp -rf logconf/. /etc/logrotate.d/
service cron reload
service cron restart

# install keepalive
dpkg -i debs/*.deb
# cp -f conf/monitor.sh /etc/keepalived/
# sudo chmod  a+x /etc/keepalived/monitor.sh
# cp -f conf/keepalived.conf /etc/keepalived/
cp -f conf/rc.local /etc/rc.local
chmod a+x /etc/rc.local


# 针对desktop
desktop_image=$( echo `ls -l vdidesktop-desktop* | awk '{ print $9 }'`)
old_desktop_contanier=$(echo `docker ps --format "{{.Names}}" | grep vdidesktop-desktop`)
if [ "${desktop_image}"T = ""T ];
then
  echo 'cannot find vdidesktop-desktop-x.x.x.x.docker'
else
  docker load -i ${desktop_image}
  echo ${desktop_image} 'load ok'
  if [ "${old_desktop_contanier}"T = ""T ];
  then
    echo 'no old'
  else
    docker kill ${old_desktop_contanier}
    sleep 1
    docker rm ${old_desktop_contanier}
    echo 'rm old_desktop_contanier'
  fi
fi


# 针对etcd
etcd_image=$( echo `ls -l etcd* | awk '{ print $9 }'`)
old_etcd_contanier=$(echo `docker ps --format "{{.Names}}" | grep etcd`)
if [ "${etcd_image}"T = ""T ];
then
  echo 'cannot find etcd-x.x.x.x.docker'
else
  docker load -i ${etcd_image}
  echo ${etcd_image} 'load ok'
  if [ "${old_etcd_contanier}"T = ""T ];
  then
    echo 'no old'
  else
    docker kill ${old_etcd_contanier}
    sleep 1
    docker rm ${old_etcd_contanier}
    echo 'rm old_etcd_contanier'
  fi
fi


# 针对novnc
novnc_image=$( echo `ls -l novnc* | awk '{ print $9 }'`)
old_novnc_contanier=$(echo `docker ps --format "{{.Names}}" | grep novnc`)
if [ "${novnc_image}"T = ""T ];
then
  echo 'cannot find novnc-x.x.x.x.docker'
else
  docker load -i ${novnc_image}
  echo ${novnc_image} 'load ok'
  if [ "${old_novnc_contanier}"T = ""T ];
  then
    echo 'no old'
  else
    docker kill ${old_novnc_contanier}
    sleep 1
    docker rm ${old_novnc_contanier}
    echo 'rm vdidesktop-novnc'
  fi
fi


# 加载镜像
# docker load -i vdidesktop-desktop-3.1.1.0123.docker
# docker load -i etcd-3.1.1.docker
# docker load -i novnc-websocket-3.docker


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

mysql_log='/var/log/mysql/mysqld.log'
if [ ! -f "${mysql_log}" ];then
  touch ${mysql_log}
fi



# 针对redis
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
