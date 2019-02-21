
show processlist和show full processlist


各个列的含义：

①.id列，用户登录mysql时，系统分配的"connection_id"，可以使用函数connection_id()查看
②.user列，显示当前用户。如果不是root，这个命令就只显示用户权限范围的sql语句
③.host列，显示这个语句是从哪个ip的哪个端口上发的，可以用来跟踪出现问题语句的用户
④.db列，显示这个进程目前连接的是哪个数据库
⑤.command列，显示当前连接的执行的命令，一般取值为休眠（sleep），查询（query），连接（connect）等
⑥.time列，显示这个状态持续的时间，单位是秒
⑦.state列，显示使用当前连接的sql语句的状态，很重要的列。state描述的是语句执行中的某一个状态。一个sql语句，以查询为例，可能需要经过copying to tmp table、sorting result、sending data等状态才可以完成
⑧.info列，显示这个sql语句，是判断问题语句的一个重要依据
