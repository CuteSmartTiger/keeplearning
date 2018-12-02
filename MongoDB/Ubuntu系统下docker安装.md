#### 拉取镜像
docker pull mongo

#### 启动容器
docker run -p 27017:27017 -v $PWD/db:/data/db -d mongo

- 命令说明：
1. -p 27017:27017 :将容器的27017 端口映射到主机的27017 端口
2. -v $PWD/db:/data/db :将主机中当前目录下的db挂载到容器的/data/db，作为mongo数据存储目录
