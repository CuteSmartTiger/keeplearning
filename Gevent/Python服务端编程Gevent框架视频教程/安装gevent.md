```shell

#!/bin/bash

# https://packaging.python.org/tutorials/installing-packages/#ensure-pip-setuptools-and-wheel-are-up-to-date
# 升级安装工具
python -m pip install --upgrade pip setuptools wheel



sudo mv /var/lib/dpkg/info  /var/lib/dpkg/info_old
sudo mkdir /var/lib/dpkg/info
sudo apt-get update
sudo apt-get -f install
sudo mv /var/lib/dpkg/info/*   /var/lib/dpkg/info_old
sudo rm -rf  /var/lib/dpkg/info
sudo mv  /var/lib/dpkg/info_old  /var/lib/dpkg/info

# 升级setup
# wget https://bootstrap.pypa.io/ez_setup.py -O - | python
 # pip install --upgrade setuptools


# 安装libeven
mkdir -p /temp/libevent
cd /temp/libevent
wget -O libevent-2.0.21-stable.tar.gz https://github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz
tar zxvf libevent-2.0.21-stable.tar.gz
cd libevent-2.0.21-stable
./configure -prefix=/usr
make && make install
# 测试libevent是否安装成功：
# ls -al /usr/lib | grep libevent



# 官方文档：https://pypi.org/project/greenlet/#description
# 安装greenlet
cd /temp/
wget https://files.pythonhosted.org/packages/f8/e8/b30ae23b45f69aa3f024b46064c0ac8e5fcb4f22ace0dca8d6f9c8bbe5e7/greenlet-0.4.15.tar.gz
tar -zxvf greenlet-0.4.15.tar.gz
cd greenlet-0.4.15
sudo python setup.py install


# 安装gevent
cd /temp/
wget https://files.pythonhosted.org/packages/ed/27/6c49b70808f569b66ec7fac2e78f076e9b204db9cf5768740cff3d5a07ae/gevent-1.4.0.tar.gz
tar -zxvf gevent-1.4.0.tar.gz
cd gevent-1.4.0
sudo python setup.py install


```


export HTTP_PROXY=''
export HTTP_PROXYS=''
pip install greenlet
pip install gevent 

```


easy_install greenlet
easy_install gevent
```


```
sudo apt-get install build-essential
sudo apt-get install python-dev
sudo apt-get install libxml2-de;
sudo apt-get install libxslt1-dev
sudo apt-get install libssl-dev
apt-get install -y libffi-dev

```



https://pypi.org/project/greenlet/#files

下载包：https://files.pythonhosted.org/packages/f8/e8/b30ae23b45f69aa3f024b46064c0ac8e5fcb4f22ace0dca8d6f9c8bbe5e7/greenlet-0.4.15.tar.gz
