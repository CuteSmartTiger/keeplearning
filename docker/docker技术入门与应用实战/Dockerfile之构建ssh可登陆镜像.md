#### vim Dockerfile_ssh
```
FROM centos:6
MAINTAINER LIUHU
ENV ROOT_PASSWORD 123456
RUN yum install -y openssh-server
RUN echo $ROOT_PASSWORD |passwd --stdin root
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
CMD ["/usr/sbin/sshd", "-D"]
EXPOSE 22
```

####  创建镜像
docker build -t ssh:v1 -f ./Dockerfile_ssh .



#### 创建容器并运行
docker run -itd --name ssh -p 2222:22 ssh:v1
