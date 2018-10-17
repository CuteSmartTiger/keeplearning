### docker 三剑客
- docker-machine   docker容器服务
- docker-compose   docker相关的脚本，简化容器的启动
- docker-swarm     容器的集群技术，主要有两个作用，一个是容器集群技术，二则是网络共享技术



注意:docker 不适合使用容器集群，尤其是有状态的，比如数据库  缓存，复制同步时压力大，docker swarm 主要用于网络共享通信

特点：去中心化
管理方式：多个swarm manager ，多个swarm worker

### 创建swarm 集群
docker swarm init
可以添加的参数：
--listen-addr ip:port  管理者节点，可以指定主机上一个具体的IP作为管理者节点IP，必存
--advertise-addr ip    广播地址，其他节点访问这个地址可以加入docker swarm集群


### 加入swarm集群
在管理者节点上执行：
docker swarm join-token manager
会输入字符串指令，以manager身份加入集群
同一时间只有一个manager节点管理集群，挂掉了则另外一个顶上


docker swarm join-token worker
会输出字符串指令，在其他虚拟机输入指令，以worker身份加入集群
worker节点用于运行容器执行指令


### 查看swarm集群中的节点
docker node ls  查看集群节点，只可以在manager节点执行
ID后面加*的为当前管理集群的节点


### 查看swarm集群网络
docker network ls  
其中有一个ingress的网络，用来管理swarm集群的


### 创建共享网络: 用于管理docker与docker容器之间的业务通信
docker network create -d overlay --attachable swarm_test
共享网络名称叫：swarm_test


### docker版本升级(若提示没--attachable命令则考虑升级docker)
```
参考网址：https://blog.csdn.net/mungo/article/details/54632686

添加源
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
补充说明：tee指令会从标准输入设备读取数据，将其内容输出到标准输出设备，同时保存成文件。

更新源
sudo apt-get update

安装docker
sudo apt-get install docker-engine

验证安装是否正确
docker run hello-world

查看版本信息
docker version
docker --version
docker -v

查看docker信息
docker info

````


- 创建pxc镜像
参见pxc


- 创建数据卷
docker volume create v1
docker volume create backup

### 使用共享网络创建pxc容器
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -v v1:/var/lib/mysql -v backup:/data --privileged --name=node1 --net=swarm_test pxc
第一个节点初始化时时间比较长，可以等待连接数据成功后再创建后续的

docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -v v1:/var/lib/mysql  --privileged --name=node1 --net=swarm_test pxc

补充说明：
若将node1容器停掉，然后无法重启，则需要把容器删除，然后重启创建容器，并制定同步的节点，参考命令如下：
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=node2 -v v1:/var/lib/mysql  --privileged --name=node1 --net=swarm_test pxc


第一台：manager
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -v v1:/var/lib/mysql --privileged --name=mysql-41 --net=swarm_test pxc

第二台：manager
docker volume create v49
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=mysql-41 -v v49:/var/lib/mysql  --privileged --name=mysql-49 --net=swarm_test pxc

第三台：work
docker volume create v90
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=mysql-41 -v v90:/var/lib/mysql  --privileged --name=mysql-90 --net=swarm_test pxc


第四台：work
docker volume create v92
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=mysql-41 -v v92:/var/lib/mysql  --privileged --name=mysql-92 --net=swarm_test pxc


### 针对其他虚拟机
- 第二台
docker volume create v2

加入集群数据库
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=node1 -v v2:/var/lib/mysql  --privileged --name=node2 --net=swarm_test pxc

添加后进行连接测试

关闭防火墙，互相ping

- 第三台
docker volume create v3

加入集群数据库
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=node1 -v v3:/var/lib/mysql  --privileged --name=node3 --net=swarm_test pxc

添加后进行连接测试

关闭防火墙，互相ping


此处待测定：
技巧点：为了减少全量复制同步给数据库集群带来的压力，可以把全量备份的数据拿到新节点还原，然后再加入集群
第四台虚拟机的容器
我现在假设第一台虚拟机坏掉了（容器被我停掉了），我现在新增第四台虚拟机，需要先在现有运行的设备上生成token，然后将第四台加入集群，然后执行以下命令
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=node2 -v v1:/var/lib/mysql  --privileged --name=node4 --net=swarm_test pxc

docker volume ls
docker inspect volume_name   查看获知数据库的位置



docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -e CLUSTER_NAME=PXC -e XTRABACKUP_PASSWORD=123123 -e CLUSTER_JOIN=node2 -v v90:/var/lib/mysql  --privileged --name=node90 --net=swarm_test pxc




### 离开集群
前提：相关容器已经删除
work节点离开集群
docker swarm leave

若果目的明确需要删除所有manager节点，可以针对所有的节点执行：
docker swarm leave --force
若只针对一部分manager节点，则执行步骤为manager 降级为 worker -> 退出集群 -> 移除节点
docker node demote node_name
docker swarm leave
docker node rm  node_name
_
### 删除集群节点
删除任何节点必须停止她的docker服务
service docker stop

启动docker服务
service docker start


manager节点必须降级为worker节点然后再删除

节点降级
docker node demote node_name


删除节点（节点状态为down），可以执行service docker stop将节点状态变为down
docker node rm  node_name
