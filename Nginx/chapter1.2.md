#环境调式
- 确认事项
可连接公网
ping www.baidu.com

- apt-get 更新（这两者的区别）
sudo apt-get update
sudo apt-get upgrade

- iptables规则关闭
```
查看
iptables -L

关闭
iptables -F

再次查看
iptables -t nat -L

若有则关闭
iptables -t nat -F
```
- 停止selinux
```
查看
getenforce

setenforce 0
```

#### 安装两项
- centos平台编译环境使用如下指令
centos 7.0 以上:
yum -y install gcc gcc-c++ autoconf pcre pcre-devel make automake
yun -y install wget httpd-tools vim


- ububtu平台编译环境可以使用以下指令:
sudo apt-get update
[转换为Ubuntu下安装，参考文章：](https://www.cnblogs.com/wyd168/p/6636529.html)

```
apt-get install build-essential
apt-get install libtool

查看gcc-c++包的位置：
dpkg -L gcc-c++

sudo apt-get -y install wget apache2-utils vim
```

- 一次初始化：
cd/opt
一次性创建多个目录，目录名称之间用空格隔开
mkdir app dowoload logs work backup
