1. 数据卷

将宿主机目录挂载到容器目录。数据卷特点：
	在容器启动初始化时，如果容器使用的宿主机挂载点有数据，这些数据就会拷贝到容器中。
	数据卷可以在容器直接共享和重用。
	可以直接对数据卷里的内容进行修改。
	数据卷的变化不会影响镜像的更新。
	卷会一直存在，即使挂载数据卷的容器已经删除。

示例：
docker run -itd --name web01 -v /container_data/web:/data Ubuntu
注：/container_data/web为宿主机目录，/data是容器中目录，目录不存在会自动创建

2. 容器数据卷
将一个运行的容器作为数据卷，让其他容器通过挂载这个容器实现数据共享。示例：
docker run -itd -v /data --name dvdata ubuntu
docker run -itd --name web01 --volumes-from dvdata ubuntu
