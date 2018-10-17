任何节点  可读可写

第一步：
- DNS
```

 vi  /etc/resolv.conf

nameserver 8.8.8.8
nameserver 8.8.4.4
nameserver 192.168.3.1
nameserver 192.168.1.1

```


第二步：下载防火墙设置
- irewall-cmd 是 firewalld的字符界面管理工具，firewalld是centos7的一大特性
```
apt install firewalld
```
- Ubuntu
```
```




- 加速器配置
若不配置加速度，则后续更新时时无法更新或者下载安装相关的包
```
curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io


docker pull percona/percona-xtradb-cluster

docker pull docker.io/percona/percona-xtradb-cluster

docker search
```

```
docker network create --subnet=172.18.0.0/16 net1
```
