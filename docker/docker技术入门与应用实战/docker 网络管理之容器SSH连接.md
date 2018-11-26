
docker run -itd --name test01 centos

docker attach test01

yum install openssh-server


passwd root
123456

docker commit test01 centos6_ssh



##### 指定网络为none则docker inspect 查看均为空信息
docker run -itd --net=none --name test02 centos6_ssh


##### 不指定网络则默认分配"Gateway": "172.17.0.1","IPAddress":"172.17.0.2"
docker run -itd  --name test02-1 centos6_ssh



pipework br0 test01 192.168.1.88/24@192.168.1.1



此处待定
docker run -itd --name test03 -p 2222:22 centos6_ssh


启动ssh(实测启动失败)
/etc/init.d/sshd start
