1.查询create user 语法
mysql> \h create user;
新增password_option选项
password_option: {
    PASSWORD EXPIRE           #设置密码过期，用户在下次登录时密码设置一个新的密码
  | PASSWORD EXPIRE DEFAULT   #设置账号使用全局配置的过期策略  default_password_lifetime 
  | PASSWORD EXPIRE NEVER     #密码永不过期
  | PASSWORD EXPIRE INTERVAL N DAY #密码在N天后过期
  | PASSWORD HISTORY DEFAULT  #设置账号使用全局配置的密码历史策略 password_history
  | PASSWORD HISTORY N        #设置禁止重用最新N次的密码
  | PASSWORD REUSE INTERVAL DEFAULT #基于时间控制密码是否可以重用，default表示使用全避默认值password-reuse-interval
  | PASSWORD REUSE INTERVAL N DAY #基于时间控制密码是否可以重用，禁止重用N天前的密码
}

2.新建用户
create user test@'localhost' identified by '123456' PASSWORD history 1;
新建用户test@'localhost',并且设置密码历史策略为1，也就是禁止前一次的密码。
select * from mysql.user where user='test'\G
查看user表中的记录，主要看password_reuse_history列的值

3.在另一个session中登录用户,无授权，所以看不到任何库表

4.在session1中设置用户过期
alter user test@'localhost' password expire;

5.在session2中再次登录
[root@node-5 ~]# mysql -utest -p 
Enter password: 
mysql> show databases;
ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
mysql> 
提示密码过期，重新设置密码
mysql> alter user user() identified by '123456';
ERROR 3638 (HY000): Cannot use these credentials for 'test@localhost' because they contradict the password history policy
修改为原密码，报错
mysql> alter user user() identified by '654321';
修改成功