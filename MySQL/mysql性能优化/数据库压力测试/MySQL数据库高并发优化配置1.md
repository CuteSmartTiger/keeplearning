获取服务器的性能

- mysql 配置文件的优化

 mysqlslap -a -c 300 -i 10 -uroot -p123123
 -c 并发测试，可以得知每秒处理的最大请求
 -i 多轮测试，获取的结果更为准确

mysql 配置文件的优化之max_connections
```

set global max_connections=100;
SHOW VARIABLES LIKE 'max_connections';

root@007490428b22:/#  mysqlslap -a -c 300 -i 10 -uroot -p123123
mysqlslap: [Warning] Using a password on the command line interface can be insecure.
Benchmark
	Average number of seconds to run all queries: 0.827 seconds
	Minimum number of seconds to run all queries: 0.741 seconds
	Maximum number of seconds to run all queries: 0.939 seconds
	Number of clients running queries: 300
	Average number of queries per client: 0



set global max_connections=400;
SHOW VARIABLES LIKE 'max_connections';

root@007490428b22:/#  mysqlslap -a -c 500 -i 10 -uroot -p123123
mysqlslap: [Warning] Using a password on the command line interface can be insecure.
mysqlslap: Error when connecting to server: 1040 Too many connections
mysqlslap: Error when connecting to server: 1040 Too many connections
mysqlslap: Error when connecting to server: 1040 Too many connections
mysqlslap: Error when connecting to server: 1040 Too many connections
Benchmark
	Average number of seconds to run all queries: 1.780 seconds
	Minimum number of seconds to run all queries: 1.696 seconds
	Maximum number of seconds to run all queries: 1.957 seconds
	Number of clients running queries: 500
	Average number of queries per client: 0


set global max_connections=1000;
SHOW VARIABLES LIKE 'max_connections';

root@007490428b22:/#  mysqlslap -a -c 500 -i 10 -uroot -p123123
mysqlslap: [Warning] Using a password on the command line interface can be insecure.
Benchmark
	Average number of seconds to run all queries: 1.803 seconds
	Minimum number of seconds to run all queries: 1.610 seconds
	Maximum number of seconds to run all queries: 2.150 seconds
	Number of clients running queries: 500
	Average number of queries per client: 0



```



- [MySQL数据库高并发优化配置](https://www.cnblogs.com/musings/p/5913157.html)

```

在Apache, PHP, mysql的体系架构中，MySQL对于性能的影响最大，也是关键的核心部分。对于Discuz!论坛程序也是如此，MySQL的设置是否合理优化，直接 影响到论坛的速度和承载量！同时，MySQL也是优化难度最大的一个部分，不但需要理解一些MySQL专业知识，同时还需要长时间的观察统计并且根据经验 进行判断，然后设置合理的参数。

 下面我们了解一下MySQL优化的一些基础，MySQL的优化我分为两个部分，一是服务器物理硬件的优化，二是MySQL自身(my.cnf)的优化。

一、服务器硬件对MySQL性能的影响

① 磁盘寻道能力（磁盘I/O）,以目前高转速SCSI硬盘(7200转/秒)为例，这种硬盘理论上每秒寻道7200次，这是物理特性决定的，没有办法改变。 MySQL每秒钟都在进行大量、复杂的查询操作，对磁盘的读写量可想而知。所以，通常认为磁盘I/O是制约MySQL性能的最大因素之一，对于日均访问量 在100万PV以上的Discuz!论坛，由于磁盘I/O的制约，MySQL的性能会非常低下！解决这一制约因素可以考虑以下几种解决方案：  使用RAID-0+1磁盘阵列，注意不要尝试使用RAID-5，MySQL在RAID-5磁盘阵列上的效率不会像你期待的那样快。

②CPU 对于MySQL应用，推荐使用S.M.P.架构的多路对称CPU，例如：可以使用两颗Intel Xeon 3.6GHz的CPU，现在我较推荐用4U的服务器来专门做数据库服务器，不仅仅是针对于mysql。

③物理内存对于一台使用MySQL的Database Server来说，服务器内存建议不要小于2GB，推荐使用4GB以上的物理内存，不过内存对于现在的服务器而言可以说是一个可以忽略的问题，工作中遇到了高端服务器基本上内存都超过了16G。

二、 MySQL自身因素

当解决了上述服务器硬件制约因素后，让我们看看MySQL自身的优化是如何操作的。对MySQL自身的优化主要是对其配置文件 my.cnf中的各项参数进行优化调整。下面我们介绍一些对性能影响较大的参数。  由于my.cnf文件的优化设置是与服务器硬件配置息息相关的，因而我们指定一个假想的服务器硬件环境：

下面，我们根据以上硬件配置结合一份已经优化好的my.cnf进行说明：


#vim /etc/my.cnf以下只列出my.cnf文件中[mysqld]段落中的内容，其他段落内容对MySQL运行性能影响甚微，因而姑且忽略。
 代码如下   复制代码
[mysqld]
port = 3306
serverid = 1
socket = /tmp/mysql.sock
skip-locking
#避免MySQL的外部锁定，减少出错几率增强稳定性。
skip-name-resolve
#禁止MySQL对外部连接进行DNS解析，使用这一选项可以消除MySQL进行DNS解析的时间。但需要注意，如果开启该选项，则所有远程主机连接授权都要使用IP地址方式，否则MySQL将无法正常处理连接请求！
back_log = 384
#back_log 参数的值指出在MySQL暂时停止响应新请求之前的短时间内多少个请求可以被存在堆栈中。  如果系统在一个短时间内有很多连接，则需要增大该参数的值，该参数值指定到来的TCP/IP连接的侦听队列的大小。不同的操作系统在这个队列大小上有它自 己的限制。 试图设定back_log高于你的操作系统的限制将是无效的。默认值为50。对于Linux系统推荐设置为小于512的整数。
key_buffer_size = 256M
#key_buffer_size指定用于索引的缓冲区大小，增加它可得到更好的索引处理性能。对于内存在4GB左右的服务器该参数可设置为256M或384M。注意：该参数值设置的过大反而会是服务器整体效率降低！
max_allowed_packet = 4M
thread_stack = 256K
table_cache = 128K
sort_buffer_size = 6M
#查询排序时所能使用的缓冲区大小。注意：该参数对应的分配内存是每连接独占，如果有100个连接，那么实际分配的总共排序缓冲区大小为100 × 6 ＝ 600MB。所以，对于内存在4GB左右的服务器推荐设置为6-8M。
read_buffer_size = 4M
#读查询操作所能使用的缓冲区大小。和sort_buffer_size一样，该参数对应的分配内存也是每连接独享。
join_buffer_size = 8M
#联合查询操作所能使用的缓冲区大小，和sort_buffer_size一样，该参数对应的分配内存也是每连接独享。
myisam_sort_buffer_size = 64M
table_cache = 512
thread_cache_size = 64
query_cache_size = 64M
# 指定MySQL查询缓冲区的大小。可以通过在MySQL控制台观察，如果Qcache_lowmem_prunes的值非常大，则表明经常出现缓冲不够的 情况；如果Qcache_hits的值非常大，则表明查询缓冲使用非常频繁，如果该值较小反而会影响效率，那么可以考虑不用查询缓 冲；Qcache_free_blocks，如果该值非常大，则表明缓冲区中碎片很多。
tmp_table_size = 256M
max_connections = 768
#指定MySQL允许的最大连接进程数。如果在访问论坛时经常出现Too Many Connections的错误提 示，则需要增大该参数值。
max_connect_errors = 10000000
wait_timeout = 10
#指定一个请求的最大连接时间，对于4GB左右内存的服务器可以设置为5-10。

thread_concurrency = 8
#该参数取值为服务器逻辑CPU数量*2，在本例中，服务器有2颗物理CPU，而每颗物理CPU又支持H.T超线程，所以实际取值为4*2=8

skip-networking
#开启该选项可以彻底关闭MySQL的TCP/IP连接方式，如果WEB服务器是以远程连接的方式访问MySQL数据库服务器则不要开启该选项！否则将无法正常连接！
table_cache=1024
#物理内存越大,设置就越大.默认为2402,调到512-1024最佳
innodb_additional_mem_pool_size=4M
#默认为2M
innodb_flush_log_at_trx_commit=1
#设置为0就是等到innodb_log_buffer_size列队满后再统一储存,默认为1
innodb_log_buffer_size=2M
#默认为1M
innodb_thread_concurrency=8
#你的服务器CPU有几个就设置为几,建议用默认一般为8
key_buffer_size=256M
#默认为218，调到128最佳
tmp_table_size=64M
#默认为16M，调到64-256最挂
read_buffer_size=4M
#默认为64K
read_rnd_buffer_size=16M
#默认为256K
sort_buffer_size=32M
#默认为256K
thread_cache_size=120
#默认为60
query_cache_size=32M


如果从数据库平台应用出发，我还是会首选myisam.

PS:可能有人会说你myisam无法抗太多写操作，但是我可以通过架构来弥补，说个我现有用的数据库平台容量：主从数据总量在几百T以上，每天十多亿 pv的动态页面，还有几个大项目是通过数据接口方式调用未算进pv总数，(其中包括一个大项目因为初期memcached没部署,导致单台数据库每天处理 9千万的查询)。而我的整体数据库服务器平均负载都在0.5-1左右。

MyISAM和InnoDB优化：

key_buffer_size – 这对MyISAM表来说非常重要。如果只是使用MyISAM表，可以把它设置为可用内存的 30-40%。合理的值取决于索引大小、数据量以及负载 — 记住，MyISAM表会使用操作系统的缓存来缓存数据，因此需要留出部分内存给它们，很多情况下数据比索引大多了。尽管如此，需要总是检查是否所有的 key_buffer 都被利用了 — .MYI 文件只有 1GB，而 key_buffer 却设置为 4GB 的情况是非常少的。这么做太浪费了。如果你很少使用MyISAM表，那么也保留低于 16-32MB 的 key_buffer_size 以适应给予磁盘的临时表索引所需。

innodb_buffer_pool_size – 这对Innodb表来说非常重要。Innodb相比MyISAM表对缓冲更为敏感。MyISAM可以在默认的 key_buffer_size 设置下运行的可以，然而Innodb在默认的 innodb_buffer_pool_size 设置下却跟蜗牛似的。由于Innodb把数据和索引都缓存起来，无需留给操作系统太多的内存，因此如果只需要用Innodb的话则可以设置它高达 70-80% 的可用内存。一些应用于 key_buffer 的规则有 — 如果你的数据量不大，并且不会暴增，那么无需把 innodb_buffer_pool_size 设置的太大了。

innodb_additional_pool_size – 这个选项对性能影响并不太多，至少在有差不多足够内存可分配的操作系统上是这样。不过如果你仍然想设置为 20MB(或者更大)，因此就需要看一下Innodb其他需要分配的内存有多少。

innodb_log_file_size 在高写入负载尤其是大数据集的情况下很重要。这个值越大则性能相对越高，但是要注意到可能会增加恢复时间。我经常设置为 64-512MB，跟据服务器大小而异。

innodb_log_buffer_size 默 认的设置在中等强度写入负载以及较短事务的情况下，服务器性能还可 以。如果存在更新操作峰值或者负载较大，就应该考虑加大它的值了。如果它的值设置太高了，可能会浪费内存 — 它每秒都会刷新一次，因此无需设置超过1秒所需的内存空间。通常 8-16MB 就足够了。越小的系统它的值越小。

innodb_flush_logs_at_trx_commit 是否为Innodb比MyISAM慢1000倍而头大？看来也许你忘了修改这个参数了。默认值是 1，这意味着每次提交的更新事务（或者每个事务之外的语句）都会刷新到磁盘中，而这相当耗费资源，尤其是没有电池备用缓存时。很多应用程序，尤其是从 MyISAM转变过来的那些，把它的值设置为 2 就可以了，也就是不把日志刷新到磁盘上，而只刷新到操作系统的缓存上。日志仍然会每秒刷新到磁盘中去，因此通常不会丢失每秒1-2次更新的消耗。如果设置 为 0 就快很多了，不过也相对不安全了 — MySQL服务器崩溃时就会丢失一些事务。设置为 2 指挥丢失刷新到操作系统缓存的那部分事务。

table_cache — 打开一个表的开销可能很大。例如MyISAM把MYI文件头标志该表正在使用中。你肯定不希望这种操作太频繁，所以通常要加大缓存数量，使得足以最大限度 地缓存打开的表。它需要用到操作系统的资源以及内存，对当前的硬件配置来说当然不是什么问题了。如果你有200多个表的话，那么设置为 1024 也许比较合适（每个线程都需要打开表），如果连接数比较大那么就加大它的值。我曾经见过设置为 100,000 的情况。

thread_cache — 线程的创建和销毁的开销可能很大，因为每个线程的连接/断开都需要。我通常至少设置为 16。如果应用程序中有大量的跳跃并发连接并且 Threads_Created 的值也比较大，那么我就会加大它的值。它的目的是在通常的操作中无需创建新线程。

query_cache — 如果你的应用程序有大量读，而且没有应用程序级别的缓存，那么这很有用。不要把它设置太大了，因为想要维护它也需要不少开销，这会导致MySQL变慢。通 常设置为 32-512Mb。设置完之后最好是跟踪一段时间，查看是否运行良好。在一定的负载压力下，如果缓存命中率太低了，就启用它。

sort_buffer_size –如果你只有一些简单的查询，那么就无需增加它的值了，尽管你有 64GB 的内存。搞不好也许会降低性能。


```
