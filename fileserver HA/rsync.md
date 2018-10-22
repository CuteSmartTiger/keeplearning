真正的inotify+rsync实时同步
https://www.cnblogs.com/jackyyou/p/5681126.html



rsync网址：
https://www.samba.org/ftp/rsync/


作废：
```

rsync安装配置
http://www.ttlsa.com/linux/rsync-install-on-linux/


配置：
/opt/rsync

此目录下下载压缩文件：
wget  https://www.samba.org/ftp/rsync/rsync-patches-3.1.3.tar.gz

解压到指定目录
tar –xzvf rsync-3.0.6.tar.gz –C ../software/


/opt/rsync/software# tar -xzvf /opt/rsync/rsync-patches-3.1.3.tar.gz

/configure --prefix=opt/rsync/ –disable-ipv6
```


### Ubuntu自带

参考文章：
https://blog.csdn.net/u010391029/article/details/51111987
https://www.linuxprobe.com/rsync-installation-configuration.html

查看系统已经安装的rsync包
dpkg --get-selections | grep rsync

安装
sudo apt-get install rsync

查看版本
rsync --version


/etc/rsyncd.conf是rsync的默认配置文件，该配置文件不存在，需要编辑内容



vi /etc/rc.local
usr/bin/rsync --daemon
写入 /etc/rc.local 文件以便在每次启动服务器时运行 rsync 服务




#### 编辑配置文件
vi /etc/rsyncd.conf
配置文件内容：
```
# Minimal configuration file for rsync daemon
# See rsync(1) and rsyncd.conf(5) man pages for help
# This line is required by the /etc/init.d/rsyncd script

# GLOBAL OPTIONS 全局参数
uid = root                  
#运行RSYNC守护进程的用户        
gid = root                 
#运行RSYNC守护进程的组

use chroot = yes             
#掠过软连接            
read only = no      

#limit access to private LANs
hosts allow=192.168.6.0/255.255.255.0   
#172.16.0.0/255.255.0.0 192.168.1.0/255.255.255.0 10.0.1.0/255.255.255.0
hosts deny=*                
#禁止连接主机                
max connections = 5        
 #最大连接数      

pid file = /var/run/rsyncd.pid             
#pid文件的存放位置
lock file = /var/run/rsync.lock            
#锁文件的存放位置
motd file = /etc/rsyncd.motd         
#指定一个消息文件，当客户连接服务器时该文件的内容显示给客户
log file = /var/log/rsync.log               
#日志记录文件的存放位置

# MODULE OPTIONS
[backup]                   
#这里是认证的模块名，在client端需要指定           
path = /opt/docker/mnt/uploads/                      
list=no                                  
ignore errors                              
auth users = root          
#认证的用户名，如果没有这行则表明是匿名，此用户与系统无关                         
comment =  root home               
#这个模块的注释信息  

secrets file = /etc/rsyncd.secrets   
#密码和用户名对比表，密码文件自己生成

```

#### 配置rsync密钥，secrets file指定的文件
vi /etc/rsyncd.secrets
内容：
```
root:123123    #账号：密码，一行一个用户
```
修改密码文件的权限为600
chown root:root /etc/rsyncd.secrets
chmod 600 /etc/rsyncd.secrets

#### 建立连接到服务器的客户端看到的欢迎信息文件
vi /etc/rsyncd.motd


### 启动rsync server
1. RSYNC服务端启动的两种方法
(1) 启动rsync服务端（独立启动）

[root@linuxprobe ~]#/usr/bin/rsync --daemon
```
此处出现问题：rsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1183) [sender=3.1.1]

请手写rsync --daemon
主要空格或者-字符不正确导致
``
(2) 启动rsync服务端 （有xinetd超级进程启动）

[root@linuxprobe ~]# /etc/rc.d/init.d/xinetd reload
2. 加入rc.local
在各种操作系统中，rc文件存放位置不尽相同，可以修改使系统启动时把rsync --daemon加载进去。
[root@linuxprobe ~]# vim /etc/rc.local
加入一行/usr/bin/rsync --daemon

3. 检查rsync是否启动
若输出显示state为LISTEN，表示为等待接受链接的状态，说明rsync已经启动。


- 查看是否启动
netstat -a | grep rsync

出现报错getnameinfo failed
解决方法：注册对应IP和主机名到DNS中


### 配置rsync client 端
设定密码
vi /etc/rsyncd.secrets
123123

修改权限：
chown root.root /etc/rsyncd.secrets
chmod 600 /etc/rsyncd.secrets

###client连接SERVER
- 从SERVER端取文件

/usr/bin/rsync -avzP --delete root@192.168.6.46::backup /opt/docker/mnt/uploads/ --password-file=/etc/rsyncd.secrets

- 向SERVER端上传文件

/usr/bin/rsync -avzP  --password-file=/root/rsync.pas  /home/backup linuxprobe@192.168.0.217::backup
这个命令将把本地机器/home/backup目录下的所有文件（含子目录）全部备份到RSYNC SERVER（172.20.0.6）的backup模块的设定的备份目录下。
请注意如果路径结束后面带有"/",表示备份该目录下的东东，但不会创建该目录，如不带"/"则创建该目录。


```
#### 最终情况说明：
最后同步，虽然信号连接成功，但是密码认证时出现错误，并且无法找到错误源，
