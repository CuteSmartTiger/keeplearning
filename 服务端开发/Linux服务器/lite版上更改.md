sudo apt-get remove vim-common -y
sudo apt-get install vim -y


cat >> /etc/network/interfaces <<- EOF
source /etc/network/interfaces.d/*
auto lo
iface lo inet loopback
auto eth0
iface eth0 inet static
address 192.168.3.242
netmask 255.255.255.0
gateway 192.168.3.1
dns-nameserver 8.8.8.8
EOF


systemd-analyze critical-chain


# 通过sudo raspi-config配置ssh的开启
#sed -i '/exit/i\sudo /etc/init.d/ssh start' /etc/rc.local


systemctl disable dhcpcd.service
systemctl disable hciuart.service
systemctl disable raspi-config.service

systemctl disable wifi-country.service
systemctl disable  rc-local.service

systemctl disable networking.service

dphys-swapfile.service
keyboard-setup.service
rsyslog.service


systemctl enable dhcpcd.service

```SHELL
cat >> jie_mian.sh  <<- EOF
#!/usr/bin/env bash

sudo apt update
sudo apt install xorg -y
sudo apt install lxde openbox -y
sudo apt install pix-icons pix-plym-splash pixel-wallpaper -y
sudo apt install raspberrypi-ui-mods -y
EOF
```


分析
root@raspberrypi:~# systemd-analyze blame
          5.072s hciuart.service
          2.879s networking.service
          1.497s raspi-config.service
          1.494s dev-mmcblk0p2.device
           728ms rc-local.service
           643ms keyboard-setup.service
           567ms dphys-swapfile.service
           413ms systemd-fsck@dev-disk-by\x2dpartuuid-8f81046b\x2d01.service
           391ms systemd-timesyncd.service
           370ms rsyslog.service
           334ms systemd-logind.service
           321ms avahi-daemon.service
           302ms wpa_supplicant.service
           292ms systemd-modules-load.service
           275ms systemd-udev-trigger.service
           269ms plymouth-start.service
           236ms systemd-fsck-root.service
           234ms systemd-tmpfiles-setup-dev.service
           232ms run-rpc_pipefs.mount
           215ms systemd-udevd.service
           174ms systemd-journald.service
           162ms triggerhappy.service
           153ms wifi-country.service
           148ms dhcpcd.service
           140ms rng-tools.service
           136ms systemd-remount-fs.service
           136ms systemd-journal-flush.service
           128ms kmod-static-nodes.service
           125ms sys-kernel-debug.mount
           113ms bluetooth.service
           106ms systemd-tmpfiles-setup.service
           104ms ssh.service
