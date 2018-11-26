#### 临时生效：
```
# 网桥名称
br_name=br0
# 添加网桥
brctl addbr $br_name
# 给网桥设置IP
ip addr add 192.168.1.120/24 dev $br_name # 删除已存在的eth0网卡配置
ip addr del 192.168.1.120/24 dev eth0
# 激活网桥
ip link set $br_name up
# 添加eth0到网桥
brctl addif $br_name eth0
还需要在Docker启动时桥接这个网桥：
vi /etc/default/docker
DOCKER_OPTS="-b=br0"
service docker restart
```


#### 永久生效：
vi /etc/network/interfaces
```
auto eth0
iface eth0 inet static
auto br0
iface br0 inet static
    address 192.168.1.120
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 192.168.1.1
    bridge_ports eth0
```
重启后开始生效
