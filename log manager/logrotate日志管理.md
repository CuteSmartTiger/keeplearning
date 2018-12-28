#### logrotate 简介

logrotate是一个日志管理程序，用来把旧的日志文件删除（备份），并创建新的日志文件，这个过程称为“转储”。

我们可以根据日志的大小，或者根据其使用的天数来转储。

logrotate 的执行由crond服务实现。在/etc/cron.daily目录中，有个文件logrotate，它实际上是个shell script，用来启动logrotate。logrotate程序每天由cron在指定的时间（/etc/crontab）启动。因此，使用ps是无法查看到logrotate的。如果它没有起来，就要查看一下crond服务有没有在运行。在执行logrotate时，需要指定其配置文件/etc/logrotate.conf。

每个存放在/etc/logrotate.d目录里的文件，都有上面格式的配置信息。在{}中定义的规则，如果与logrotate.conf中的冲突，以/etc/logrotatate.d/中的文件定义的为准。

#### 参数

-?或--help 　在线帮助。
-d或--debug 　详细显示指令执行过程，便于排错或了解程序执行的情况。
-f或--force 　强行启动记录文件维护操作，纵使logrotate指令认为没有需要亦然。
-s<状态文件>或--state=<状态文件> 　使用指定的状态文件。
-v或--version 　显示指令执行过程。
-usage 　显示指令基本用法。

#### 配置文件
```
执行文件：/usr/sbin/logrotate
主配置文件：/etc/logrotate.conf
自定义配置文件：/etc/logrotate.d/*.conf

/etc/logrotate.d/ - 通常一些第三方软件包，会把自己私有的配置文件，也放到这个目录下。如yum，zabbix-agent，syslog等。

修改配置文件后，并不需要重启服务。
由于logrotate实际上只是一个可执行文件，不是以daemon运行。
d.日志分割原理

系统会按照计划的频率运行logrotate,通常是每天。大多数的Linux发行版本上，计划每天运行脚本位于/etc/cron.daily/logrotate

当logrotate 运行的时候，它会读取自身配置文件来决定需要分割日志文件的路径，分割日志文件的频率及保留多少日志存档。
```
#### 常用参数
```
compress                               通过gzip 压缩转储以后的日志

nocompress                             不必压缩时，用这个参数

nocreate                               不建立新的日志文件

delaycompress 和 compress              一起使用时，转储的日志文件到下一次转储时才压缩 nodelaycompress 覆盖 delaycompress 选项，转储同时压缩。

ifempty                                即使是空文件也转储，这个是 logrotate 的缺省选项。

notifempty                              如果是空文件的话，不转储

missingok                               如果日志不存在则忽略该警告信息

prerotate/endscript                     在转储以前需要执行的命令能放入这个对，这两个关键字必须独立成行

postrotate/endscript                    在转储以后需要执行的命令能放入这个对，这两个关键字必须独立成行

rotate                                  命令指定分割日志的数量，也就是保留多少个日志，当新的分割日志产生时，会删除最老的

weekly   daily  monthly  yearly         定义分割频度

size                                                          定义文件大小
```
#### logrotate主配置文件详解
```
# see "man logrotate" for details
# rotate log files weekly
weekly                      #每周轮转一次
# keep 4 weeks worth of backlogs
rotate 4                    #保留四个日志文件
# create new (empty) log files after rotating old ones
create                      #rotate后，创建一个新的空文件
# uncomment this if you want your log files compressed
#compress                   #默认是不压缩的
# RPM packages drop log rotation information into this directory

include /etc/logrotate.d    #这个目录下面配置文件生效
# no packages own wtmp — we’ll rotate them here
/var/log/wtmp {             #定义/var/log/wtmp这个日志文件；
    monthly                 #每月轮转一次，取代了上面的全局设定的每周轮转一次；
    minsize 1M              #定义日志必须要大于1M大小才会去轮转；
    create 0664 root utmp   #新的日志文件的权限，属主，属主；
    rotate 1                #保留一个，取代了上面的全局设定的保留四个；
}
/var/log/btmp {             #定义/var/log/btmp这个日志文件；
    missingok               #如果日志丢失, 不报错；
    monthly
    create 0600 root utmp
    rotate 1
}

记住，在 /etc/logrotate.d/ 目录下的应用配置文件继承所有的 /etc/logrotate.conf 默认参数
g.nginx日志logrotate配置说明

##解释nginx 的logrotate 配置
##固定格式，支持通配符匹配
/var/log/nginx_*.log {              
    daily                       ##每天转储一次
    missingok                   ##如果日志不存在则忽略该警告信息
    dateext                     ##转储以后以日期作为后缀
    ifempty                     ##即使是空文件也转储，这个是 logrotate 的缺省选项。
    rotate 20                   ##保留20份日志文件；log.1...log.20
    sharedscripts               ##共享脚本,下面的postrotate <s> endscript中的脚本只执行一次即可；
    postrotate                  ##
        /netpas/nginx/sbin/nginx -c /netpas/nginx/conf/nginx.conf -p /netpas/nginx -s reopen > /dev/null 2>/dev/null || true
        /netpas/nginx/sbin/nginx -c /netpas/nginx/conf/nginx_udp.conf -p /netpas/nginx -s reopen > /dev/null 2>/dev/null || true
    endscript
}
postrotate <s> endscript  #日志轮换过后指定指定的脚本，endscript参数表示结束脚本；
Logrotate每次分割文件后会运行 postrotate 后的命令。最通常的作用是让应用重启，以便切换到新的日志文件。
第一部分是匹配的文件模式，可以是通配符，注意：如果对应的日志不存在会报错，中断处理，可以自行用调试模式测试。（可以添加missingok缓解）

{ ... } 花括号里面的就是具体的指令参数了，logrotate支持一些hook预处理，可以在执行之前或者之后调用命令或者自己的脚本。
````
