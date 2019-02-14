推荐号文章 [对mysql的高并发优化配置的一些思考](http://blog.51cto.com/xiaozhagn/2073900)


```
[mysqld]
# 线程并发小于64时可以按默认的0设置， 根际实际情况设置
innodb_thread_concurrency=128

# 指定MySQL允许的最大连接进程数,若经常出现Too Many Connections的错误提示，则需要增大该参数值。
max_connections=1000;


```



```

mysql自身的优化

总的来说还是自身因素影响的比较多，我们可以通过修改my.cnf配置文件来对mysql进行进一步的优化。我们可以通过修改mysql的参数使得mysql拥有更可靠的性能。下面是我的数据库配置，自己通过百度谷歌，找很多配置选项的解析（配置适合mysql5.5以上的版本），然后总结。希望对你有帮助。（注意一下优化配置均在【mysqld】选项下配置，不要搞错成【mysql】）


[mysqld]
back_log = 300
binlog_format = MIXED
character-set-server=utf8mb4
long_query_time = 1
log-bin=/databack/data_logbin/mysql_binlog
innodb_log_file_size=2G
innodb_log_buffer_size=4M
innodb_buffer_pool_size=4G
#innodb_file_per_table = ON
innodb_thread_concurrency=8
innodb_flush_logs_at_trx_commit=2
#innodb_additional_mem_pool_size=4M
join_buffer_size = 8M
key_buffer_size=256M
max_connections = 1000
max_allowed_packet = 4M
max_connect_errors = 10000
myisam_sort_buffer_size = 64M
port = 3306
query_cache_type=1
query_cache_size = 64M
read_buffer_size=4M
read_rnd_buffer_size=4M
server-id = 1
skip-external-locking
slow_query_log = 1
#skip-name-resolve
#skip-networking
sort_buffer_size = 8M
socket = /tmp/mysql.sock
table_open_cache=1024
thread_cache_size = 64
thread_stack = 256K
tmp_table_size=64M
wait_timeout = 10


下面是对上面配置的解析：



back_log = 300：该参数的值表示在MySql的连接数据达到#max_connections 时，在它暂时停止响应新请求之前的短时间内有300个请求可以被存在堆栈中，即新来的请求将会被存在堆栈中，以等待某一连接释放资源，该堆栈的数量即back_log，等 mysql处理完其他请求之后会对其作出响应，如果等待连接的数量超过#back_log，将不被授予连接资源。你可以合理的设置你的back_log，但是该值不要高于操作系统的限制的值。系统的默认值为50。Linux系统一般设置小于512的整数。



binlog_format = MIXED：配置主从模式下，选取同步的模式，Mysql主从的复制可以有三种复制类型，分别是:语句的复制STATEMEN,行的复制ROW和混合类型的复制MIXED，语句的复制顾名思义就是在主服务器上执行的SQL语句，在从服务器上执行同样的语句，行的复制就是把改变的内容复制过去，而不是把命令在从服务器上执行一遍。默认采用基于语句的复制，一旦发现基于语句的无法精确的复制时，就会采用基于行的复制,配置，复制类型可以通过binlog_format =在配置文件上配置



character-set-server=utf8mb4 ：utf-8编码可能2个字节、3个字节、4个字节的字符，但是MySQL的utf8编码只支持3字节的数据，而移动端的表情数据是4个字节的字符。如果直接往采用utf-8编码的数据库中插入表情数据，Java程序中将报SQL异常utf8mb4编码是utf8编码的超集，兼容utf8，并且能存储4字节的表情字符。 采用utf8mb4编码的好处是，存储与获取数据的时候，不用再考虑表情字符的编码与解码问题。



long_query_time = 1：设置慢查询响应的时间，记录超过1秒的SQL执行语句。



log-bin=/databack/data_logbin/mysql_binlog ：设置二进制日志的存放路径，如果不设置系统会默认存放到mysql的目录下，建议创建新的目录来存放二进制日志，且该目录不要同数据库同个目录，存放目录拥有者为mysql。



innodb_log_file_size=2G ：在高写入负载尤其是大数据集的情况下很重要。这个值越大则性能相对越高，跟据服务器大小而异。这是redo日志的大小。redo日志被用于确保写操作快速而可靠并且在崩溃时恢复。在MySQL 5.5，redo日志的总尺寸被限定在4GB(默认可以有2个log文件)。而MySQL 5.6里可以设置允许大于4G。你可以一开始就把它设置成4G。这个值的设置其实是可以计算的 你可以通过命令SHOW GLOBAL STATUS的输出看Innodb_os_log_written的值，把该值除以1024*1024 得到的结果是每分钟处理的redo日志大小，然后再乘以60得到每小时处理的日志大小，因为在5.5以上版本都是默认有两个日志重做日志文件ib_logfile0和ib_logfile1，所得到结果再除以2，再取整就是你的redo该设置大小了。



innodb_log_buffer_size=4M：默认为1M，在默认的设置在中等强度写入负载以及较短事务的情况下，服务器性能还可以。如果存在更新操作峰值或者负载较大，就应该考虑加大它的值了。在 InnoDB在事务提交前，并不将改变的日志写入到磁盘中，因此在大事务中，可以减轻磁盘I/O的压力。通常情况下，如果不是写入大量的超大二进制数据，4MB-8MB已经足够了。



innodb_buffer_pool_size=4G：这配置对Innodb表来说非常重要。该参数主要作用是缓存innodb表的索引，数据，插入数据时的缓冲由于Innodb把数据和索引都缓存起来，因此在配置该参数时，可以设置它高达60-80% 的可用内存（官网是建议的也是系统内存的80%左右）。缓冲池是数据和索引缓存的地方这能保证你在大多数的读取操作时使用的是内存而不是硬盘。一般配置的值是5-6GB(8GB内存)，19-25GB(32GB内存)，38-50GB(64GB内存)仅供参考。



#innodb_file_per_table = ON：在5.6中，该选项属性默认值是ON，由于对新建的表有影响，所以在之前的版本中你需要把它设置成ON。这项设置告知InnoDB是否需要将所有表的数据单独放在一个.ibd文件，这样做的好处是使得每个表都有自已独立的表空间。每个表的数据和索引都会存在自已的表空间中。也实现单表在不同的数据库中移动，且空间可以回收。



innodb_thread_concurrency=8：指服务器逻辑线程数可以设置成与系统一样数量，参数可配置成逻辑CPU数量的两倍。

系统CPU查看命令如下：

查看逻辑CPU个数：

#cat /proc/cpuinfo |grep "processor"|sort -u|wc –l


查看物理CPU个数：

# cat /proc/cpuinfo | grep "physical id" |sort -u|wc -l


查看每个物理CPU内核个数：

# cat /proc/cpuinfo |  grep "cpu cores" |uniq


innodb_flush_logs_at_trx_commit=2：系统默认值是 1，但是这样设置会使得提交更新事务都会刷新到磁盘中，会造成资源耗费。所以需要值设置为 2，这样就不用不把日志刷新到磁盘上，而只刷新到操作系统的缓存上。但然啦也可以设置为0， 这样设置是很快，但也造成了相对的不安全，会导致MySQL服务器崩溃时就会丢失一些事务。而设置为 2 刚好尼补了。



#innodb_additional_mem_pool_size=4M：该参数默认为1M适当调整该参数的大小以确保所有数据都能存放在内存中提高访问效率的，主要用来存放Innodb的内部目录，这个值不用分配太大，系统可以自动调。在mysql5.6.3可以忽略。



join_buffer_size = 8M：表示#联合查询操作所能使用的缓冲区大小。



key_buffer_size=256M：指定索引缓冲区的大小，它决定索引处理的速度，你可以设置成系统的物理内存的1/4，它主要针对的是MyISAM引擎，但是设置大少不要超过4G，不然会出现问题。



max_connections = 1000：设置置MySQL的最大连接，按你实际情况适当设置就好。如果你经常看到‘Too many connections'错误，是因为max_connections的值太低了，所以需要设置更高的链接数，如果max_connection值被设高之后的缺陷是当服务器运行超过设置阈值或更高的活动事务时会变的没有响应。



max_allowed_packet = 4M：这个参数mysql消息缓冲区的大小，如果这个过小可能会影响到部分操作，默认是1M，一般设置成4-16M就可以了。



max_connect_errors = 10000：表示如果有同一个主机访问的参数值超出该参数值个数的中断错误连接，则该主机将被禁止连接。如需对该主机进行解禁，执行：FLUSH HOST。



myisam_sort_buffer_size = 64M：这个参数默认是8M，表示MyISAM表发生变化时重新排序所需的缓冲，一般64M就已经足够了。



port = 3306：表示使用3306来做mysql启动端口



query_cache_type=1：表示控制缓存的类型，有三个参数可选（0、1、2）设置为0，表示缓存没有应用，也就相当于禁用了，设置为1，表示缓存所有的结果，设置为2表示只缓存在select语句中通过SQL_CACHE指定需要缓存的查询。



query_cache_size=32M：参数表示mysql查询结果的缓冲区大小，一般不建议设置太大，因为设置太大会增加开销，一般设置成32M-256M左右即可，设置参数一般为2的倍数。



read_buffer_size=4M：表示按顺序查询操作包括读、查询等操作所能使用的缓冲区大小，和sort_buffer_size一样，该参数对应的分配内存也是每连接独享，一般不建议太大，对于4G到16G内存的服务器2M-8M就可以了。



read_rnd_buffer_size=4M：表示是MySQL的随机读缓冲区大小。当任意顺序读取行时将分配一个随机读取缓冲区，进行排序查询时，便分配随机缓冲作为该操作的缓冲区大小，同样的对于4G到16G内存的服务器2M-8M就可以了。



server-id = 1：表示做主从同步所定义的serverid，作为master的server_id必须必slave端的要小，越小表示优先级越高，但是在同个网段内的mysql服务，不允许设置同样的sever_id。参数可设参考范围（1-200）。



skip-external-locking：开启该选项表示避免MySQL的外部锁定，减少出错几率增强稳定性，适用于单服务器环境。



slow_query_log = 1：开启慢查询日志，作用于慢查询日志,顾名思义,就是查询慢的日志。



skip-name-resolve：禁止MySQL对外部连接进行DNS解析，使用这一选项可以消除MySQL进行DNS解析的时间。但需要注意，如果开启该选项，则所有远程主机连接授权都要使用IP地址方式，否则MySQL将无法正常处理连接请求。



skip-networking：开启该选项可以彻底关闭MySQL的TCP/IP连接方式，如果WEB服务器是以远程连接的方式访问MySQL数据库服务器则不要开启该选项，否则将无法正常连接。



sort_buffer_size = 8M：表示查询排序时所能使用的缓冲区大小。它直接与实时连接的个数 有关，实时连接的个数乘以sort_buffer_size的大小就是实际分配的总共排序缓冲区大小。所以，对于内存在4GB-8G左右的服务器可以设置为6-16M。



socket = /tmp/mysql.sock：mysql.sock 文件作用主要是server和client在同一台服务器，当使用本地连接时，就会使用socket进行连接，该文件一般是放在/var/lib/mysql/mysql.sock下，也常常使用ln –s 在/tmp目录下做软连接。



table_open_cache=1024：table_cache主要用于设置table高速缓存的数量。由于每个客户端连接都会至少访问一个表，因此此参数的值与max_connections有关。你可以通过命令show variables like '%open%'; 查看open_files_limit参数,大量使用MyISAM的环境里，应该保证open_files_limit表类型至少是table_cache的二到三倍，调到512-1024最佳。



thread_cache_size = 64 ：这个变量值表示的是可以重新利用保存在缓存中线程的数量,当断开连接时如果缓存中还有空间,那么客户端的线程将被放到缓存中,如果线程重新被请求，那么请求将从缓存中读取,如果缓存中是空的或者是新的请求，那么这个线程将被重新创建,如果有很多新的线程，增加这个值可以改善系统性能.通过比较 Connections 和 Threads_created 状态的变量，可以看到这个变量的作用 根据物理内存设置规则可以做以下配置2G-4G可以设置为16-64左右，当然大于4G的服务器，设置64也已经足够了。



thread_stack = 256K：表示每个连接线程被创建时，MySQL给它分配的内存大小，对于8-16G的服务器设置成256K就可以了，再大一点的，可以适当增加呢。



tmp_table_size=64M：表示定义一个临时表的大小，该值默认为16M，可调到64-256最佳，线程独占，太大可能内存不够造成I/O堵塞，如果动态页面可以适当调大点。



wait_timeout = 100：表示指定一个请求的最大连接时间，该值过大会导致，MySQL里大量的SLEEP进程无法及时释放，拖累系统性能，不过也不能把这个指设置的过小，否则你可能会遭遇到“MySQL has gone away”之类的问题。  系统默认是8个小时，感觉太大，可以设置小点。



3、总结

    预防Mysql病发的情况，是每个企业所要面对的事情，大数据的到来，更加使得mysql的性能要求更高，所以对mysql的优化升级，也是迫在眉睫。以上是本人总结，仅仅提供参考，希望能帮到你


```
