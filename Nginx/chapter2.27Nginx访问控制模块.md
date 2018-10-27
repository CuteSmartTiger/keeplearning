#### 基于ip的访问控制
http_access_module

```
Syntax:allow address|CIDR|unix:|all;
Default:
Context:http,server,location,limit_execpt

```

与之对应
```
Syntax:deny address|CIDR|unix:|all;
Default:
Context:http,server,location,limit_execpt
```

配置文件：
进行模式匹配，匹配地址中根目录下的admin.html
#    location ~ ^/admin.html {
#        root   /opt/app/code;
#        deny 183.157.13.30;
#        allow all;
#        index  index.html index.htm;
#    }


- 查询自己电脑的公网ip
www.ip138.com


有局限性，解决方法：
方法一：使用http_x_forward_for
http_x_forward_for = clientIP,Proxy(1)IP,Proxy(2)IP,Proxy(3)IP

方法二：geo模块


方法三：通过http自定义头部变量传递



#### 基于用户的信任登录
http_auth_basic_module

string一则用来作为提示信息，二则作为开启on
```
Syntax:auth_basic string|off;
Default:uth_basic off;
Context:http,server,location,limit_execpt

```

```
#file为文件路径，文件存储密码用户等信息
Syntax:auth_basic_user_file file;
Default:
Context:http,server,location,limit_execpt
```
[参考官网：](http://nginx.org/en/docs/)



在/etc/nginx/下创建加密的密码文件
htpassword -c ./auth_conf username password

查看文件的另一种方法：
more ./auth_conf


配置示例：
```
#    location ~ ^/admin.html {
#        root   /opt/app/code;
#        auth_basic 'show string to replace on';
#        auth_basic_user_file /etc/nginx/auth_conf;
#        index  index.html index.htm;
#    }
```


- 检查与启动
```
nginx -tc /etc/nginx/nginx.conf

nginx -s reload -c /etc/nginx/nginx.conf

nginx -c /etc/nginx/nginx.conf
```

局限性:
操作复杂，用户密码多难管理

解决方向：
1.Nginx结合LUA实现高效验证
2.Nginx与LDAP打动，利用nginx-auth-ldap模块
