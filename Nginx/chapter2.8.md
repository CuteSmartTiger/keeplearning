### 基本参数
#### 安装目录
- 查看Nginx文件位置：
dpkg -L Nginx

- 日志轮询切割
/etc/logrotate.d/nginx  

- Nginx主配置文件位置：
/etc/nginx
/etc/nginx/nginx.conf
/etc/nginx/conf.d
/etc/nginx/conf.d/default.conf

- cgi,fastcgi配置
/etc/nginx/fast_params
/etc/nginx/uwsgi_params
/etc/nginx/scgi_params

- 编码转换映射文件(用的比较少)
/etc/nginx/koi-utf
/etc/nginx/koi-win
/etc/nginx/win-utf

- 设置http协议的Content-Type与扩张名的对应关系
/etc/nginx/mime.types

- 用于配置出系统守护进程管理器管理方式
/usr/bin/systemd/system/nginx-debug.service
/usr/bin/systemd/system/nginx.service
/etc/sysconfig/nginx
/etc/sysconfig/nginx-debug

- Nginx 模块目录
/usr/lib64/nginx/modules
/etc/nginx/modules

- nginx 命令，服务的启动管理的终端命令
/usr/sbin/nginx
/usr/sbin/nginx-debug

- Nginx 缓存
/var/cache/nginx

- nginx 日志
/var/log/nginx

- nginx 帮助手册
/usr/share/

#### 编译参数
见chapter2.9


- Nginx基本配置语法
