第一步：
- DNS
```
vi  /etc/resolv.conf

nameserver 8.8.8.8
nameserver 8.8.4.4
nameserver 192.168.3.1
nameserver 192.168.1.1
```

```
vi /etc/sysctl.conf
中添加
net.ipv4.ip_forward = 1

重启
systemctl restart network
实际执行中这个失败
```

第二步：
- 防火墙相关设置
```
sudo apt-get install ufw
sudo ufw enable
sudo ufw default deny



开放端口
sudo ufw allow 3306/tcp

开放22端口以便putty或winscp打开
sudo ufw allow 22/tcp

关闭端口
sudo ufw deny 32/tcp


查看状态
sudo ufw status
```

第三步：安装镜像
- percona/percona-xtradb-cluster
```
docker pull percona/percona-xtradb-cluster

docker tag percona/percona-xtradb-cluster pxc
```

第四步：
自定义网段的作用：创建net1网段，则在同一网段中的容器可以通信
创建网段
docker network create --subnet=172.18.0.0/16 net1

查看网段
docker network inspect net1

显示所有网段
docker network ls

删除前需要断开与容器的连接
删除
docker network rm


第五步：
创建数据卷

docker volume create --name v1
docker volume create --name v2
docker volume create --name v3
docker volume create --name v4
docker volume create --name v5
docker volume create --name backup

数据卷是被设计用来持久化数据的，它的生命周期独立于容器，Docker不会在容器被删除后自动删除数据卷，
并且也不存在垃圾回收这样的机制来处理没有任何容器引用的数据卷。如果需要在删除容器的同时移除数据卷。
可以在删除容器的时候使用 docker rm -v 这个参数，实测加入-v并没有用


###第六步
- 含热备份  优化方向：了解字段中的含义
docker run 命令下的含义
理解以下的含义：
-d: 后台运行容器，并返回容器ID；

-e CLUSTER_NAME=PXC: 设置环境变量
-v suzhu:rongqi    将宿主机文件映射到容器，即宿主文件内容，容器中可以看到
-i: 以交互模式运行容器，通常与 -t 同时使用
-t: 为容器重新分配一个伪输入终端，通常与 -i 同时使用；

‐‐privileged
--name=node1: 为容器指定一个名称
--net="bridge": 指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型；
‐‐ip

-p 3306:3306：将主机(宿主)的 3306 端口映射到容器的3306端口，即通过访问宿主机的端口可以访问容器的端口
-e MYSQL_ROOT_PASSWORD=123456：初始化 root 用户的密码


docker run -d -p 3306:3306 ‐e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -v v1:/var/lib/mysql -v backup:/data --privileged --name=node1 --net=net1 --ip 172.18.0.2 pxc

docker run -d -p 3307:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=node1 -v v2:/var/lib/mysql -v backup:/data --privileged --name=node2 --net=net1 --ip 172.18.0.3 pxc

docker run -d -p 3308:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=node1 -v v3:/var/lib/mysql -v backup:/data --privileged --name=node3 --net=net1 --ip 172.18.0.4 pxc

docker run -d -p 3309:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=node1 -v v4:/var/lib/mysql -v backup:/data --privileged --name=node4 --net=net1 --ip 172.18.0.5 pxc

docker run -d -p 3310:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=node1 -v v5:/var/lib/mysql -v backup:/data --privileged --name=node5 --net=net1 --ip 172.18.0.6 pxc


- 不含热备份
```
创建第一个容器时需要多等一会，可以用datagrip进行测试，看可否创建实例成功
docker run ‐d ‐p 3306:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐v v1:/var/lib/mysql ‐‐privileged ‐‐name=node1 ‐‐net=net1 ‐‐ip 172.18.0.2 pxc

docker run ‐d ‐p 3307:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐e CLUSTER_JOIN=node1 ‐v v2:/var/lib/mysql ‐‐privileged ‐‐name=node2 ‐‐net=net1 ‐‐ip 172.18.0.3 pxc

docker run ‐d -p 3308:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐e CLUSTER_JOIN=node1 ‐v v3:/var/lib/mysql ‐‐privileged ‐‐name=node3 ‐‐net=net1 ‐‐ip 172.18.0.4 pxc

docker run ‐d ‐p 3309:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐e CLUSTER_JOIN=node1 ‐v v4:/var/lib/mysql ‐‐privileged ‐‐name=node4 ‐‐net=net1 ‐‐ip 172.18.0.5 pxc

docker run ‐d ‐p 3310:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐e CLUSTER_JOIN=node1 ‐v v5:/var/lib/mysql ‐‐privileged ‐‐name=node5 ‐‐net=net1 ‐‐ip 172.18.0.6 pxc



node1 挂了后怎么办
docker run ‐d ‐p 3306:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐e CLUSTER_JOIN=node5 ‐v v1:/var/lib/mysql ‐‐privileged ‐‐name=node1 ‐‐net=net1 ‐‐ip 172.18.0.2 pxc
```

第七部：负载均衡   将一个节点处理数据变为多个节点处理数据库
- Haproxy 镜像下载
```
docker search haproxy

docker pull haproxy
```
- haproxy 配置文件
```
编写配置文件：


上传至 目录下：
/home/soft/haproxy/
```
#创建第1个Haproxy负载均衡服务器
docker run -it -d -p 4001:8888 -p 4002:3306 -v /home/soft/haproxy:/usr/local/etc/haproxy --name h1 --privileged --net=net1 --ip 172.18.0.7 haproxy

docker run -it -d -p 4011:8888 -p 4012:3306 -v /home/soft/haproxy:/usr/local/etc/haproxy --name h1 --privileged --net=net1 --ip 172.18.0.7 haproxy

#进入h1容器，启动Haproxy
docker exec -it h1 bash
haproxy -f /usr/local/etc/haproxy/haproxy.cfg

```
new选项中选择console然后创建用户与密码
数据库创建用户：密码为空
CREATE USER 'haproxy'@'%' IDENTIFIED BY '';

网页输入：
http://192.168.6.91:4001/dbs
用户与密码配置文件中有

```
- KEEPALIVED 争抢虚拟IP
```
进入haproxy容器
docker exec -it h1 bash

更新
apt-get update

安装
apt-get install keepalived

apt-get install vim



备注：

启动
service keepalived start

停止
service keepalived stop

重启
service keepalived restart
```


/etc/keepalived/keepalived.conf
```
vrrp_instance  VI_1 {
    state  MASTER
    interface  ens33
    virtual_router_id  51
    priority  100
    advert_int  1
    authentication {
        auth_type  PASS
        auth_pass  123123
    }
    virtual_ipaddress {
        172.18.0.201
    }
}
VI_1  配置信息的名字
state  MASTER 或者slave  定义master则主服务要抢占虚拟IP，salve与备用服务（backup）不会抢占
nterface  eth0  :docker 网卡  ens33为宿主机网卡      eth0为容器的网卡
virtual_router_id  51    keepalived的ip，要求0-255之间
priority  100   数值越大  权重越大  越优先抢占IP
advert_int  1   master与backup节点之间同步检查时的时间间隔，单位秒。主备之间必须一致
authentication  定义心跳检测登录的账号与密码
virtual_ipaddress  网eth0中写入虚拟IP，可以设置多个虚拟IP，每行一个，此IPdocker内部可见，出了docker则看不见
```
- 启动keepalived
```
容器内部
service keepalived start

在容器外部检测
ping 172.18.0.201
```


#创建第2个Haproxy负载均衡服务器
docker run -it -d -p 4003:8888 -p 4004:3306 -v /home/soft/haproxy:/usr/local/etc/haproxy --name h2 --privileged --net=net1 --ip 172.18.0.8 haproxy

#进入h2容器，启动Haproxy
docker exec -it h2 bash
haproxy ‐f /usr/local/etc/haproxy/haproxy.cfg


###在宿主机安装keepalived
apt-get install -y keepalived

宿主机配置文件  /etc/keepalived/keepalived.conf
service keepalived start
