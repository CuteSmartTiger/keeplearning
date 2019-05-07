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




sed -i '/exit/i\sudo /etc/init.d/ssh start' /etc/rc.local
