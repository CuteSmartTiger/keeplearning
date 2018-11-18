cd /opt/soft/

DNS客户端解析文件resolv.conf配置
vi /etc/resolv.conf
```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

wget http://download.redis.io/releases/redis-5.0.0.tar.gz

tar -xzf redis-5.0.0.tar.gz

建立软连接，方便以后升级
ln -s redis-5.0.0.tar.gz Redis

cd redis-5.0.0



sudo apt-get install build-essential

#apt install make-guile
#apt install make

make

make install

提示：
make[1]: Leaving directory '/opt/soft/redis-5.0.0/src

cd src


ll  | grep redis-


测试
redis-cli -h 127.0.0.1 -p 6379

重新开一个端口
set liu hu
ping
exit
del liu


ps -ef | grep redis-server | grep -v grep
