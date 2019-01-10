##### 老板的级别： /etc/crontab
cron是一个Linux定时执行工具，可以在无需人工干预的情况下运行作业。在Ubuntu server 下，cron是被默认安装并启动的。通过/etc/crontab文件内的命令来执行定时任务

不同的目录下对应着主管定时的任务脚本
```
ununtu 通过调用 run-parts 命令，定时运行四个目录下的所有脚本。
1）/etc/cron.hourly，目录下的脚本会每个小时让执行一次，在每小时的2分钟时运行；
2）/etc/cron.daily，目录下的脚本会每天让执行一次，在每天0点17分时运行；
3）/etc/cron.weekly，目录下的脚本会每周让执行一次，在每周第七天的3点56分时运行；
4）/etc/cron.mouthly，目录下的脚本会每月让执行一次，在每月19号的5点32分时运行；
当然，以上的时间均是系统默认时间，可以根据自己的需求进行修改。

```



#### cron 服务的启动与停止
在Ubuntu 9.10下，cron是被默认安装并启动的。而 ubuntu 下启动，停止与重启cron，均是通过调用/etc/init.d/中的脚本进行。命令如下：
1）service cron start  /*启动服务*/

2）service cron stop /*关闭服务*/

3）service cron restart / *重启服务*/
4）service cron reload /*重新载入配置*/
5) service cron status /* 查看定时任务的状态*/
6） 可以通过以下命令查看cron是否在运行（如果在运行，则会返回一个进程ID）：
pgrep cron





####   crontab命令
```
crontab 命令用于安装、删除或者列出用于驱动cron后台进程的表格。也就是说，用户把需要执行的命令序列放到crontab文件中以获得执行，每个用户都可以有自己的crontab文件。以下是这个命令的一些参数与说明：
1）crontab -u /*设定某个用户的cron服务*/
2）crontab -l /*列出某个用户cron服务的详细内容*/
3）crontab -r /*删除某个用户的cron服务*/
4）crontab -e /*编辑某个用户的cron服务*/
参数名称 含义 示例
-l 显示用户的Crontab文件的内容 crontabl –l
-i 删除用户的Crontab文件前给提示 crontabl -ri
-r 从Crontab目录中删除用户的Crontab文件 crontabl -r
-e 编辑用户的Crontab文件 crontabl -e
/etc/crontab文件语法如下：
Minute Hour Day Month Dayofweek command
分钟 小时 天 月 天每星期 命令
每个字段代表的含义及取值范围如下：
Minute ：分钟（0-59），表示每个小时的第几分钟执行该任务
Hour ： 小时（1-23），表示每天的第几个小时执行该任务
Day ： 日期（1-31），表示每月的第几天执行该任务
Month ： 月份（1-12），表示每年的第几个月执行该任务
DayOfWeek ： 星期（0-6，0代表星期天），表示每周的第几天执行该任务
Command ： 指定要执行的命令（如果要执行的命令太多，可以把这些命令写到一个脚本里面，然后在这里直接调用这个脚本就可以了，调用的时候记得写出命令的完整路径）
在这些字段里，除了“Command”是每次都必须指定的字段以外，其它字段皆为可选字段，可视需要决定。对于不指定的字段，要用“*”来填补其位置。同时，cron支持类似正则表达式的书写，支持如下几个特殊符号定义：

“*” ,代表所有的取值范围内的数字；
“/” , 代表”每”（“*/5”，表示每5个单位）；
“-” , 代表从某个数字到某个数字（“1-4”，表示1-4个单位）；
“,” ,分开几个离散的数字；
举例如下：

5 * * * * ls /*指定每小时的第5分钟执行一次ls命令*/
30 5 * * * ls /*指定每天的 5:30 执行ls命令*/
30 7 8 * * ls /*指定每月8号的7：30分执行ls命令*/
50 7 * * * root run-parts /etc/cron.daily /*每天7：50以root 身份执行/etc/cron.daily目录中的所有可执行文
```


##### 新增 cron 任务
```
1.执行如下命令添加任务

# crontab -e
1）直接执行命令行，比如每隔1分钟执行date命令并将结果保存至文件/tmp/testCron.txt中，cron 格式如下：
*/1 * * * * date >> /tmp/testCron.txt

2）执行shell 脚本，比如每隔3分钟执行一次/var/backups/test.sh 文件，cron 格式如下：
*/3 * * * * /var/backups/test.sh
```
