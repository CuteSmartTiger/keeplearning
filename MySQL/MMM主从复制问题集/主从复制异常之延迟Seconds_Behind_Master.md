1. Seconds_Behind_Master  


show slave status\G的输出结果，需要监控下面三个参数：
   1）Slave_IO_Running：该参数可作为io_thread的监控项，Yes表示io_thread的和主库连接正常并能实施复制工作，No则说明与主库通讯异常，多数情况是由主从间网络引起的问题；
   2）Slave_SQL_Running：该参数代表sql_thread是否正常，YES表示正常，NO表示执行失败，具体就是语句是否执行通过，常会遇到主键重复或是某个表不存在。
   3）Seconds_Behind_Master：是通过比较sql_thread执行的event的timestamp和io_thread复制好的event的timestamp(简写为ts)进行比较，而得到的这么一个差值；
        NULL—表示io_thread或是sql_thread有任何一个发生故障，也就是该线程的Running状态是No，而非Yes。
        0 — 该值为零，是我们极为渴望看到的情况，表示主从复制良好，可以认为lag不存在。
        正值 — 表示主从已经出现延时，数字越大表示从库落后主库越多。
        负值 — 几乎很少见，我只是听一些资深的DBA说见过，其实，这是一个BUG值，该参数是不支持负值的，也就是不应该出现


实际测试：
三十万条数据，Seconds_Behind_Master大概一两秒
