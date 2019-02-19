MYSQL5.7

innodb_buffer_pool_size – 这对Innodb表来说非常重要。Innodb相比MyISAM表对缓冲更为敏感。MyISAM可以在默认的 key_buffer_size 设置下运行的可以，然而Innodb在默认的 innodb_buffer_pool_size 设置下却跟蜗牛似的。由于Innodb把数据和索引都缓存起来，无需留给操作系统太多的内存，因此如果只需要用Innodb的话则可以设置它高达 70-80% 的可用内存。一些应用于 key_buffer 的规则有 — 如果你的数据量不大，并且不会暴增，那么无需把 innodb_buffer_pool_size 设置的太大了。



set global innodb_buffer_pool_size=3087007744;


mysql> SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
+-------------------------+------------+
| Variable_name           | Value      |
+-------------------------+------------+
| innodb_buffer_pool_size | 3087007744 |
+-------------------------+------------+





set global innodb_buffer_pool_size=3087007744;

提高线程并发数有效果，当
set global innodb_thread_concurrency=16;
测试为：

mysqlslap -a -c 400 -i 10 -uroot -p123123

失败





- 说明
```



```
