cron 服务的启动与停止
在Ubuntu 9.10下，cron是被默认安装并启动的。而 ubuntu 下启动，停止与重启cron，均是通过调用/etc/init.d/中的脚本进行。命令如下：
1）service cron start  /*启动服务*/

2）service cron stop /*关闭服务*/

3）service cron restart / *重启服务*/
4）service cron reload /*重新载入配置*/
可以通过以下命令查看cron是否在运行（如果在运行，则会返回一个进程ID）：
# pgrep cron


sudo service cron status
