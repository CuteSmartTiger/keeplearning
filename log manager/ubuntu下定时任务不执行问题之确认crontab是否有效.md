#### 背景
当系统日志无法定时压缩时需要查找原因：
首先查看crontab没有没有运行

##### 查看crontab是否有效
1. 创建定时任务
方法一：
crontab -e
然后再文本最后插入：
    ```
    * * * * * echo "Hello world!"
    ```


方法二：

sudo vim /var/spool/cron/crontabs/root   #注:root为当前用户名

在文件末行插入：
    ```
    * * * * * echo "Hello world!"
    ```
赋予权限
sudo chmod 0600 /var/spool/cron/crontabs/*

若后续针对此文件修改后在启动服务重载
sudo service cron reload

保存退出，并通过crontab -l查看定时任务创建成功

```
Fix it using the command

sudo chmod 600 /etc/crontab

and restart the service

sudo service cron restart
```



查看cron服务状态
sudo service cron status
发现cron服务是running的，排除


sudo service cron restart
重启cron后问题依旧，排除

于是进一步查看cron运行日志（/var/log/cron.log），但是并未找到相关文件，原因是ubuntu默认没有开cron日志，执行命令：
sudo vim /etc/rsyslog.d/50-default.conf
找到cron.log相关行，将前面注释符#去掉，保存退出，重启rsyslog：
sudo  service rsyslog  restart
执行less -10 /var/log/cron.log再次查看cron运行日志





##### 参考文章：

- [解决ubuntu下定时任务不执行问题](https://blog.csdn.net/u012129468/article/details/77926701)


- [Why crontab scripts are not working?](https://askubuntu.com/questions/23009/why-crontab-scripts-are-not-working)

- [cron[30673]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)](https://askubuntu.com/questions/1085894/cronjob-on-ubuntu-cron-info-pidfile-fd-3)
