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
只能压缩文件不能压缩目录，配置文件中必须知名文件名

```
vim /etc/logrotate.d/file

/vsr/log/file.log{
 daily                日志文件按每个月轮循 daily 每天 weakly 每星期 yealy 每年
 rotate 5               储存5个归档日志，对于第六个归档，时间最久的自动删除
 compress               以归档的文件用gzip进行压缩
mail address           把转储的日志文件发送到指定的E-mail 地址
nocompress              不需要压缩时，用这个参数
copytruncate            用于还在打开中的日志文件，把当前日志备份并截断
nocopytruncate          备份日志文件但是不截断
create 644 root root    转储文件，使用指定的文件模式创建新的日志文件
 size 20M               指定文件当天达到20M的时候才转储，可以设置为10K
 dateext                文件后加上当前日期
 }
以上的参数可以根据自己的需求而添加
```



#### Set "su" directive in config file to tell logrotate which user/group should be used for rotation
格式：su $user $group

vi /etc/logrotate.d/liuhu.log
su root root

#### 测试
调试 （d = debug）参数为配置文件，不指定则执行全局配置文件
logrotate -d /etc/logrotate.d/liuhu.conf

出现error: error opening /var/log/test.log.5.gz: No such file or directory，则也是正常

注意：logrotate都是需要使用root来执行的，（但是可以通过配置项来指定生成的日志文件为普通用户的）


实际强制执行：
强制执行（-f = force），可以配合-v(-v =verbose）使用，注意调试信息默认携带-v
logrotate -d /etc/logrotate.d/liuhu.conf


### 日志处理完执行自定义脚本
postrotate和endscript中间可以编写自定义脚本，用来对日志或者其他其定义处理，扩展性非常强；
例如由于logrotate对压缩日志可指定的时间戳只能到天，于是可以再自定义脚本里面对文件做时分等细化命名；

$ cat logrotate.conf

/tmp/output.log {        
    size 1k        
    copytruncate        
    rotate 4        
    compress        
    postrotate               
        /home/bala/myscript.sh        
    endscript
}


### 更改压缩程序
默认压缩程序使用.gz，当然可以自定义，需要制定压缩程序和后缀名；

$ cat logrotate.conf

/tmp/output.log {        
    size 1k        
    copytruncate        
    create        
    compress        
    compresscmd /bin/bzip2        
    compressext .bz2        
    rotate 4

### 清空但不删除日志文件
copytruncate的作用在于先复制一份当前日志文件用做处理，再清空源日志文件，让其继续接收日志。
当然在复制和清空的空隙可能会有若干

$ cat logrotate.conf

/tmp/output.log {        
    size 1k        
    copytruncate        
    create 700 bala bala        
    rotate 4        
    compress
}
