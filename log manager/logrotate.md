### 安装
sudo apt-get update
apt-get install logrotate cron




###备份、压缩或转储



#### 组成,以下是logrotate运行的关键点：
```
程序所在位置
/usr/bin/logrotate


默认让Cron每天执行logrotate一次
/etc/cron.daily/logrotate


全局配置文件
/etc/logrotate.conf


应用某个程序的配置文件存放目录，覆盖全局配置
/etc/logrotate.d/
```



#### 全局配置文件：/etc/logrotate.conf
weekly：表示每周处理下日志；
rotate 4：最多保持4个轮转备份，关于轮转本身后文会详述，很有意思；
create：处理完该日志文件后，新生成一个日志文件，当然尽可能是同名同权限等；
dateext：默认未加时间戳；
compress：默认不压缩；
对wtmp和btmp日志做了单独处理，同时单独的配置可以放在/etc/logrotate.d目录，或者直接放在全局配置里面；

于是当logrotate程序被执行时，按照字面意思logrotate默认是想每周处理下日志，对日志最多轮转保留4份，处理方式是不压缩也不加时间戳，处理完后再生成个同名文件。当然这些是默认设置，还对wtmp和btmp日志处理做了单独要求并且include /etc/logrotate.d目录下还有一大堆处理要求



#### 自定义配置文件存放目录/etc/logrotate.d/






#### Set "su" directive in config file to tell logrotate which user/group should be used for rotation
格式：su $user $group

vi /etc/logrotate.d/liuhu.log
su root root
