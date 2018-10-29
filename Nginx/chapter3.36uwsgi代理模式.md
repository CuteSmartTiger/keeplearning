uwsgi 针对Python

优势：
一则：安全


二则：效率

动静分离



Django框架配置uwsgi使用示例：




1.安装Python3环境 （[可以查看手记](https://www.imooc.com/article/26870)）

解压方式安装：
```
安装mysql支持
yum install mysqld mysql-devel


到官方网站，下载python3.6.2源码包
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz



解压，安装步骤如下

tar  -xvf Python-3.6.2.tgz

cd  Python-3.6.2/

./configure --prefix=/opt/python3.6
make
make install
echo "export PATH=/opt/python3.6/bin:$PATH" > /etc/profile.d/python.sh
echo $PATH
which python
mkdir ~/.python-eggs
chmod +w ~/.python-eggs
echo "export PATH=/opt/python3.6/bin:$PATH" > /etc/profile.d/python.sh
export PATH=/opt/python3.6/bin:$PATH

```

2.pip3 install Django



创建Django工程
在自己创建的app目录下执行：
/opt/python3.6/bin/django-admin.py startproject demo
在当前目录生成demo目录，然后进入此目录

进入opt/app/conf/目录下：
vim uwsgi.ini

配置：
[uwsgi]
04:48
