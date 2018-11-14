## docker 命令官方网站
https://docs.docker.com/engine/reference/commandline/docker/



#### docker
 - 查找docker中文件的路径
  ```
  touch [name]
  exit
  find /var/lib/ -name [name]
  ```
 - 其他  
  ```
  fg   让后台的运行的程序到前台
  docker stop [docker_id]   停止进程
  docker kill [docker_id]   停止进程

  docker run 创建并启动一个容器，在run后面加上-d参数，则会创建一个守护式容器在后台运行。
  docker ps -a 查看已经创建的容器
  docker ps -s 查看已经启动的容器
  docker start con_name 启动容器名为con_name的容器
  docker stop con_name 停止容器名为con_name的容器
  docker rm con_name 删除容器名为con_name的容器
  docker rename old_name new_name 重命名一个容器
  docker attach con_name 将终端附着到正在运行的容器名为con_name的容器的终端上面去，
  前提是创建该容器时指定了相应的sh执行这个命令后，按下回车键，会进入容器的命令行Shell中。

  docker logs con_name 获取容器名为con_name的容器日志
  docker inspect 查看容器的详细信息
  docker top con_name 查看容器名为con_name的容器内部的进程
  docker exec 可以用来在容器中运行一个进程

  ```


- docker  网络
```
配置一个网络节点
docker network create --subnet=172.20.0.0/16 net1

docker network ls
docker network inspect net1
docker network rm net1

```

- 容器中pxc节点映射数据目录的解决办法（创建docker卷）
```
docker volume create --name v1

docker volume inspect v1
{
       "Name": "v1",
       "Driver": "local",
       "Mountpoint": "/var/lib/docker/volumes/v1/_data",
       "Labels": {},
       "Scope": "local"
   }

docker volume rm v1

数据卷是被设计用来持久化数据的，它的生命周期独立于容器，Docker不会在容器被删除后自动删除数据卷，并且也不存在垃圾回收这样的机制来处理没有任何容器引用的数据卷。如果需要在删除容器的同时移除数据卷。
可以在删除容器的时候使用 docker rm -v 这个参数
docker volume ls

用于数据的热备份
docker volume create --name v1
```

- 只需要向PXC镜像传入运行参数就能创建出PXC容器
```
docker run ‐d ‐p 3306:3306 ‐e MYSQL_ROOT_PASSWORD=123123‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐v v1:/var/lib/mysql ‐v backup:/data ‐‐privileged ‐‐name=node1 ‐‐net=net1 ‐‐ip 172.20.0.2 pxc

```
docker run ‐d -p 3307:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐e CLUSTER_JOIN=node1 ‐v v2:/var/lib/mysql ‐v backup:/data ‐‐privileged ‐‐name=node2 ‐‐net=net1 ‐‐ip 172.20.0.3 pxc

docker run ‐d -p 3308:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐e CLUSTER_JOIN=node1 ‐v v3:/var/lib/mysql ‐v backup:/data ‐‐privileged ‐‐name=node3 ‐‐net=net1 ‐‐ip 172.20.0.4 pxc

docker run ‐d -p 3308:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐e CLUSTER_JOIN=node1 ‐v v4:/var/lib/mysql ‐v backup:/data ‐‐privileged ‐‐name=node4 ‐‐net=net1 ‐‐ip 172.20.0.5 pxc

docker run ‐d -p 3308:3306 ‐e MYSQL_ROOT_PASSWORD=123123 ‐e CLUSTER_NAME=PXC ‐e XTRABACKUP_PASSWORD=123123 ‐e CLUSTER_JOIN=node1 ‐v v5:/var/lib/mysql ‐v backup:/data ‐‐privileged ‐‐name=node5 ‐‐net=net1 ‐‐ip 172.20.0.6 pxc
