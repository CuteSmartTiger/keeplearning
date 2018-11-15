1. 改表法。
可能是你的帐号不允许从远程登陆，只能在localhost。这个时候只要在localhost的那台电脑，登入mysql后，更改 "mysql" 数据库里的 "user" 表里的 "host" 项，从"localhost"改称"%"

登录数据库：mysql -u root -p

mysql>use mysql;

mysql>update user set host = '%' where user = 'root';

mysql>select host, user from user;

mysql>FLUSH PRIVILEGES;


2. 授权法。

(1)例如，你想myuser使用mypassword从任何主机连接到mysql服务器的话。

第一步：root用户登录；mysql>mysql -u root -p rootpassword;

第二步：赋予权限；mysql>GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;

第三步：mysql>FLUSH   PRIVILEGES;

(2)如果你想允许用户myuser从ip为192.168.1.3的主机连接到mysql服务器，并使用mypassword作为密码

mysql>GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.1.3' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;

mysql>FLUSH   PRIVILEGES;

(3)如果你想允许用户myuser从ip为192.168.1.3的主机连接到mysql服务器的dk数据库，并使用mypassword作为密码

mysql>GRANT ALL PRIVILEGES ON dk.* TO 'root'@'192.168.1.3' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;

mysql>FLUSH   PRIVILEGES;
