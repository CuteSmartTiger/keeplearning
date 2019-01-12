#### 安装
apt-get install -y erlang

echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list


wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

sudo apt-get update


sudo apt-get install -y rabbitmq-server

service rabbitmq-server status



sudo rabbitmq-plugins enable rabbitmq_management

访问IP地址：15672可进入后台，默认用户名、密码均为guest


常用命令：
```
sudo chkconfig rabbitmq-server on  #添加开机启动（chkconfig一般只有redhat系统有）RabbitMQ服务
sudo service rabbitmq-server start  # 启动服务
sudo service rabbitmq-server status  # 查看服务状态
sudo service rabbitmq-server stop   # 停止服务



sudo rabbitmqctl stop   # 停止服务
sudo rabbitmqctl status  # 查看服务状态
sudo rabbitmqctl list_users # 查看当前所有用户
sudo rabbitmqctl list_user_permissions guest # 查看默认guest用户的权限
sudo rabbitmqctl delete_user guest# 删掉默认用户(由于RabbitMQ默认的账号用户名和密码都是guest。为了安全起见, 可以删掉默认用户）
sudo rabbitmqctl add_user username password # 添加新用户
sudo rabbitmqctl set_user_tags username administrator# 设置用户tag
sudo rabbitmqctl set_permissions -p / username ".*" ".*" ".*" # 赋予用户默认vhost的全部操作权限
```



登录rabbitmq报错User can only log in via localhost 解决办法：
vi /etc/rabbitmq/rabbitmq.config
[{rabbit, [{loopback_users, []}]}].
service rabbitmq-server restart


===========-----------以上安装成功==================================


#### 失败

安装Erlang   >>>>  官网 >> http://www.erlang.org/

sudo apt-get install -y  build-essential 
sudo apt-get install -y libncurses5-dev 
sudo apt-get install -y libssl-dev
sudo apt-get install -y m4 
sudo apt-get install -y unixodbc unixodbc-dev
sudo apt-get install -y freeglut3-dev libwxgtk2.8-dev 
sudo apt-get install -y xsltproc 
sudo apt-get install -y fop 
sudo apt-get install -y tk8.5

sudo apt-get install -y erlang




命令
sudo apt-get install rabbitmq-server


手动安装：

1.首先创建一个文件夹用来下载RabbitMQ
mkdir rabbitmqsoft
cd rabbitmqsoft

获取安装包（这里选择2.7.0 unix版本）

wget http://www.rabbitmq.com/releases/rabbitmq-server/v2.7.0/rabbitmq-server-generic-unix-2.7.0.tar.gz


--解压

 tar -zxvf rabbitmq-server-generic-unix-2.7.0.tar.gz
 cd rabbitmq_server-2.7.0/








sudo rabbitmq-plugins enable rabbitmq_management




- [ubuntu16.10下安装erlang和RabbitMQ](https://blog.csdn.net/a295277302/article/details/71246941)
