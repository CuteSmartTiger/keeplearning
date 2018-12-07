安装locale
sudo locale-gen zh_US.UTF-8

查看支持的字符集有哪些：
locale -a

查看当前容器使用字符集
locale

临时修改
export LANG=C.UTF-8
source /etc/profile

永久修改
Dockerfile中添加一行
ENV LANG C.UTF-8
