### 基于端口的虚拟机主机配置方式
- 查看端口使用情况
ss -luntp
或
netstat -luntp
或
netstat -ntpl


检查配置语法是否成功,其中tc顺序不能反
nginx -tc /etc/nginx/nginx.conf


停止然后启动Nginx服务


查看端口
netstat -ntpl


关闭iptables 规则
iptables -F
