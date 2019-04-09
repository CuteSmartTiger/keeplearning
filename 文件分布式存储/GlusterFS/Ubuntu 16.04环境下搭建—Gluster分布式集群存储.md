#### 前期准备
1. 服务与客户端ip
系统均为Ubuntu 16.04.1 LTS
server1:192.168.6.90
server2:192.168.6.91
client:192.168.6.93


2. 修改主机名以及修改hosts文件添加IP地址映射：（各个服务器节点都需要配置）
vi /etc/hosts
```
192.168.6.90   server1
192.168.6.91   server2
192.168.6.93   client
```
优化点：脚本直接输入大量文字

3. 在server1  server2 执行3-4步骤，安装glusterfs

sudo apt-get install glusterfs-server -y && echo '安装成功' || echo '安装失败'

4. 启动glusterfs
/etc/init.d/glusterfs-server start && netstat -anput | grep gluster && echo '启动成功' || echo '启动失败'

服务启动停止
service glusterfs-server start/stop

5. 集群关联
在构建GlusterFS集群时，需要在其中任意一台存储服务器上依次将其他存储服务器添加到集群中
添加服务进入集群
gluster peer probe server1
gluster peer probe server2

查看集群信息
gluster pool list
gluster peer status
gluster peer detach <HOSTNAME> [force]  #删除集群节点
gluster peer status  #list全部集群节点，显示除自己的其他全部节点
gluster pool list - list all the nodes in the pool (including localhost)


6. 在server1&2节点上都需要创建创建数据目录
mkdir -p /gluster/data


7. 配置数据卷
(1). 配置分布式卷

创建卷，执行以下命令时，请查看gluster pool list，并且ping server1 ,ping server2均无问题
gluster volume create GlusterFB server1:/gluster/data server2:/gluster/data force

显示成功volume create: GlusterFB: success: please start the volume to access data


启动数据卷GlusterFB
gluster volume start  GlusterFB

查看GlusterFB的配置信息
gluster volume info GlusterFB  
显示如下信息：
```SHELL
Volume Name: GlusterFB
Type: Distribute
Volume ID: b4d9ca79-2694-4ee7-85a3-04939666a682
Status: Started
Number of Bricks: 2
Transport-type: tcp
Bricks:
Brick1: server1:/gluster/data
Brick2: server2:/gluster/data
Options Reconfigured:
performance.readdir-ahead: on
```

#挂载GlusterFB卷
mount -t glusterfs 127.0.0.1:GlusterFB /opt
WARNING: getfattr not found, certain checks will be skipped..
/sbin/mount.glusterfs: according to mtab, GlusterFS is already mounted on /opt  

cd /opt/ &&  touch {a..f} && ll


在server2上查看数据卷信息
gluster volume info GlusterFB  
显示相同的信息




查看分布式存储
server1上执行
ll /gluster/data
-rw-r--r-- 2 root root    0 Apr  2 13:45 a
-rw-r--r-- 2 root root    0 Apr  2 13:45 b
-rw-r--r-- 2 root root    0 Apr  2 13:45 c



server2上执行
ll /gluster/data
-rw-r--r-- 2 root root    0 Apr  2 13:45 d


在client客户端挂载
mkdir -p /gluster/data
将指定服务器上的数据卷挂载到当前客户端的指定目录下
mount.glusterfs 192.168.6.90:GlusterFB  /gluster/data



##### 参考文章
- [GlusterFS分布式存储](https://www.cnblogs.com/huangyanqi/p/8406534.html)(推荐)
- [GlusterFS分布式存储集群-2. 使用](https://www.cnblogs.com/netonline/p/9107859.html)(推荐)
- [GlusterFS技术详解](https://czero000.github.io/2016/04/05/glusterfs-technical-explanation.html)(推荐)




```失败
fdisk -l

/dev/xvda2

mkfs.xfs  -i size=512 /dev/xvda2


mkfs.ext4 /dev/xvda2

parted /dev/xvda2

mount /dev/xvda2 /gluster/data
```
