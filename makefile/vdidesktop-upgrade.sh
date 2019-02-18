#! /bin/bash

# 日志配置文件复制
# sudo cp -f logrotate.conf /etc/
# sudo cp -rf logconf/. /etc/logrotate.d/
# sudo service cron reload
# sudo service cron restart

# install keepalive
sudo dpkg -i debs/*.deb
# sudo cp -f conf/monitor.sh /etc/keepalived/
# sudo chmod  a+x /etc/keepalived/monitor.sh
# sudo cp -f conf/keepalived.conf /etc/keepalived/
sudo cp -f conf/rc.local /etc/rc.local
sudo chmod a+x /etc/rc.local


# 针对desktop镜像更新的处理
desktop_image=$( echo `ls -l vdidesktop-desktop* | awk '{ print $9 }'`)
old_desktop_contanier=$(echo `sudo docker ps --format "{{.Names}}" | grep vdidesktop-desktop`)
if [ "${desktop_image}"T = ""T ];
then
  echo 'cannot find vdidesktop-desktop-x.x.x.x.docker'
else
  sudo docker load -i ${desktop_image}
  echo ${desktop_image} 'load ok'
  if [ "${old_desktop_contanier}"T = ""T ];
  then
    echo 'no old'
  else
    sudo docker kill ${old_desktop_contanier}
    sleep 1
    sudo docker rm ${old_desktop_contanier}
    echo 'rm old_desktop_contanier'
  fi
fi


# 针对etcd镜像更新的处理
etcd_image=$( echo `ls -l etcd* | awk '{ print $9 }'`)
old_etcd_contanier=$(echo `sudo docker ps --format "{{.Names}}" | grep etcd`)
if [ "${etcd_image}"T = ""T ];
then
  echo 'cannot find etcd-x.x.x.x.docker'
else
  sudo docker load -i ${etcd_image}
  echo ${etcd_image} 'load ok'
  if [ "${old_etcd_contanier}"T = ""T ];
  then
    echo 'no old'
  else
    sudo  docker kill ${old_etcd_contanier}
    sleep 1
    sudo docker rm ${old_etcd_contanier}
    echo 'rm old_etcd_contanier'
  fi
fi


# 针对novnc镜像更新的处理
novnc_image=$( echo `ls -l novnc* | awk '{ print $9 }'`)
old_novnc_contanier=$(echo `sudo docker ps --format "{{.Names}}" | grep novnc`)
if [ "${novnc_image}"T = ""T ];
then
  echo 'cannot find novnc-x.x.x.x.docker'
else
  sudo docker load -i ${novnc_image}
  echo ${novnc_image} 'load ok'
  if [ "${old_novnc_contanier}"T = ""T ];
  then
    echo 'no old'
  else
    sudo docker kill ${old_novnc_contanier}
    sleep 1
    sudo docker rm ${old_novnc_contanier}
    echo 'rm vdidesktop-novnc'
  fi
fi



# 针对数据库容器更新的处理
mysql_image=$( echo `ls -l *mysql* | awk '{ print $9 }'`)
mysql_map=$( echo `sudo docker ps -a | grep mysql | grep '0.0.0.0:3306->3306/tcp'`)

if [ "${mysql_map}"T = ""T ];
then
    is_mysql_exist=$(echo `docker ps -a | grep mysql`)
    if [ "${is_mysql_exist}"s = ""s ];
    then
        echo 'there is no mysql contaniner'
        sudo docker load -i ${mysql_image}
    else
        sudo docker kill vdidesktop-mysql
        sleep 1
        sudo docker rm vdidesktop-mysql
        echo 'rm mysql contaniner'
    fi
else
    echo 'mysql port has mapped, it is OK'
fi

# mysql_log='/var/log/mysql/mysqld.log'
# if [ ! -f "${mysql_log}" ];then
  # sudo touch ${mysql_log}
# fi



# 针对redis
redis_log_file='/var/log/redis'
redis_image=$( echo `ls -l *redis* | awk '{ print $9 }'`)

if [ ! -d "${redis_log_file}" ]; then
  is_redis_exist=$(echo `sudo docker ps -a | grep vdidesktop-redis`)
  if [ "${is_redis_exist}s" = "s" ];
  then
      echo 'there is no redis contaniner'
      sudo docker load -i ${redis_image}
      echo 'load redis image ok'
  else
      sudo docker kill vdidesktop-redis
      sudo docker rm vdidesktop-redis
      sleep 1
      echo 'rm redis contaniner'
  fi
else
  echo 'redis log directory has mapped, it is OK'
fi


# sudo mv /opt/docker/Makefile /opt/docker/Makefile.bak
# sudo cp Makefile.for_customer /opt/docker/Makefile
# sudo cd /opt/docker
sudo make rm-only
sudo mv Makefile.for_customer Makefile
sudo docker tag 192.168.5.8:5001/vdidesktop-desktop:active 192.168.5.8:5001/vdidesktop-desktop:old
sudo docker tag 192.168.5.8:5001/vdidesktop-desktop:latest 192.168.5.8:5001/vdidesktop-desktop:active
sudo make run
cd -
