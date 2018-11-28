如果创建容器时忘了进行端口映射，则可以iptables追加
iptables -t nat -A PREROUTING -d 192.168.1.120 -p tcp --dport 89 -j DNAT --to 172.17.0.3:80
通过宿主机89端口可以访问容器内部的80端口


查看规则
iptables -t nat -nL

apt-get install net-utils
apt-get install net-tools

ip addr

安装ping相关命令
apt-get install iputils-ping  


批量删除查找中的容器
docker rm -f $(docker ps -q -a)
