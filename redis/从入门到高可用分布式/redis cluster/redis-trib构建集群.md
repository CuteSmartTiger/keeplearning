src目录下
./redis-trib.rb create --replicas 1 127.0.0.1:8000 127.0.0.1:8001 127.0.0.1:8002 127.0.0.1:8003 127.0.0.1:8004 127.0.0.1:8005

打印匹配的进程号：
ps -ef | grep redis-server | grep 700| awk '{print $2}'

关闭匹配的进程
ps -ef | grep redis-server | grep 700| awk '{print $2}' | xargs kill


防止数据干扰，清楚data数据
/opt/soft/redis-5.0.0/data
rm -rf *


redis-server redis-7000.conf
redis-server redis-7001.conf
redis-server redis-7002.conf
redis-server redis-7003.conf
redis-server redis-7004.conf
redis-server redis-7005.conf
ps -ef | grep redis


在/opt/soft/redis-5.0.0/src/目录下
查看操作命令
./redis-trib.rb


redis新版本不支持redis-trib.rb
redis-cli --cluster  create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1

redis-cli -p 7000
cluster nodes
cluster info
