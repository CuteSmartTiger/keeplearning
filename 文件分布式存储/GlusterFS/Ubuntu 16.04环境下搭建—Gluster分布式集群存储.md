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

fdisk -l



mkfs.ext4 /dev/xvda2

parted /dev/xvda2


mount /dev/xvda2 /gluster/data
