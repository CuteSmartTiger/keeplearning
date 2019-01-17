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


mv /opt/docker/Makefile /opt/docker/Makefile.bak
cp Makefile.for_customer /opt/docker/Makefile
cd /opt/docker
make rm-only
docker tag 192.168.5.8:5001/vdidesktop-desktop:active 192.168.5.8:5001/vdidesktop-desktop:old
docker tag 192.168.5.8:5001/vdidesktop-desktop:latest 192.168.5.8:5001/vdidesktop-desktop:active
make run

cd -
