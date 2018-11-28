
```
配置固定IP
C_ID=$(docker run -itd --net=none ubuntu)
C_PID=$(docker inspect -f '{{.State.Pid}}' $C_ID)
# 创建network namespace目录并将容器的network namespace软连接到此目录，以便ip netns命令读取mkdir -p /var/run/netns
ln -s /proc/$C_PID/ns/net /var/run/netns/$C_PID
# 添加虚拟网卡veth+容器PID，类型是veth pair，名称是vp+容器PID
ip link add veth$C_PID type veth peer name vp$C_PID
# 添加虚拟网卡到br0网桥
brctl addif br0 veth$C_PID
# 激活虚拟网卡
ip link set veth$C_PID up
# 设置容器网络信息
IP='192.168.1.123/24'
GW='192.168.1.1'
# 给进程配置一个network namespace
ip link set vp$C_PID netns $C_PID
# 在容器进程里面设置网卡信息
ip netns exec $C_PID ip link set dev vp$C_PID name eth0
ip netns exec $C_PID ip link set eth0 up
ip netns exec $C_PID ip addr add $IP dev eth0
ip netns exec $C_PID ip route add default via 192.168.1.1
```
