systemctl is-enabled servicename.service #查询服务是否开机启动
systemctl enable *.service #开机运行服务
systemctl disable *.service #取消开机运行
systemctl start *.service #启动服务
systemctl stop *.service #停止服务
systemctl restart *.service #重启服务
systemctl reload *.service #重新加载服务配置文件
systemctl status *.service #查询服务运行状态



systemd-analyze critical-chain
systemd-analyze blame

systemctl disable hciuart.service

systemctl disable networking.service


systemctl disable plymouth-quit.service
systemctl disable plymouth-quit-wait.service



systemctl disable plymouth-read-write.service

systemctl disable lightdm.service


dphys-swapfile.service


systemctl disable raspi-config


sudo sysv-rc-conf

其他方式开启开机自启
echo "sudo /etc/init.d/ssh start" >> /etc/rc.local

echo "sudo /etc/init.d/lightdm start" >> /etc/rc.local
