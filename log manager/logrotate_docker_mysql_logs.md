将宿主机的sudo文件复制到容器中：
docker cp /usr/bin/sudo 42cbb4ba3f2d:/usr/bin/


另一种方法将容器中的日志都映射到宿主机上

-v /var/log/mysql:/var/log
-v /var/log/redis:/var/log
-v /var/log/vdidesktop:/var/log


/etc/logrotate.d/下编写配置文件：
针对mysql相关日志：
var/log/mysql/.log {
  rotate 5
  daily
  compress
  missingok
  notifempty
}

/var/log/apt/history.log {
  rotate 5
  daily
  compress
  missingok
  notifempty
  size 1M
}

依次配置其他



-v /var/log/vdidesktop:/var/log/vdidesktop -v /var/log/salt:/var/log/salt -v /var/log/nginx:/var/log/nginx
