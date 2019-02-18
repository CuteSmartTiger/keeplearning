1．索引作用
在索引列上，除了上面提到的有序查找之外，数据库利用各种各样的快速定位技术，能够大大提高查询效率。特别是当数据量非常大，查询涉及多个表时，使用索引往往能使查询速度加快成千上万倍。

例如，有3个未索引的表t1、t2、t3，分别只包含列c1、c2、c3，每个表分别含有1000行数据组成，指为1～1000的数值，查找对应值相等行的查询如下所示。



SELECT c1,c2,c3 FROM t1,t2,t3 WHERE c1=c2 AND c1=c3

此查询结果应该为1000行，每行包含3个相等的值。在无索引的情况下处理此查询，必须寻找3个表所有的组合，以便得出与WHERE子句相配的那些行。而可能的组合数目为1000×1000×1000（十亿），显然查询将会非常慢。

如果对每个表进行索引，就能极大地加速查询进程。利用索引的查询处理如下。

（1）从表t1中选择第一行，查看此行所包含的数据。

（2）使用表t2上的索引，直接定位t2中与t1的值匹配的行。类似，利用表t3上的索引，直接定位t3中与来自t1的值匹配的行。

（3）扫描表t1的下一行并重复前面的过程，直到遍历t1中所有的行。

在此情形下，仍然对表t1执行了一个完全扫描，但能够在表t2和t3上进行索引查找直接取出这些表中的行，比未用索引时要快一百万倍。

利用索引，MySQL加速了WHERE子句满足条件行的搜索，而在多表连接查询时，在执行连接时加快了与其他表中的行匹配的速度。

2.  创建索引
在执行CREATE TABLE语句时可以创建索引，也可以单独用CREATE INDEX或ALTER TABLE来为表增加索引。

1．ALTER TABLE
ALTER TABLE用来创建普通索引、UNIQUE索引或PRIMARY KEY索引。



ALTER TABLE table_name ADD INDEX index_name (column_list)

ALTER TABLE table_name ADD UNIQUE (column_list)

ALTER TABLE table_name ADD PRIMARY KEY (column_list)



其中table_name是要增加索引的表名，column_list指出对哪些列进行索引，多列时各列之间用逗号分隔。索引名index_name可选，缺省时，MySQL将根据第一个索引列赋一个名称。另外，ALTER TABLE允许在单个语句中更改多个表，因此可以在同时创建多个索引。

2．CREATE INDEX
CREATE INDEX可对表增加普通索引或UNIQUE索引。



CREATE INDEX index_name ON table_name (column_list)

CREATE UNIQUE INDEX index_name ON table_name (column_list)



table_name、index_name和column_list具有与ALTER TABLE语句中相同的含义，索引名不可选。另外，不能用CREATE INDEX语句创建PRIMARY KEY索引。

3．索引类型
在创建索引时，可以规定索引能否包含重复值。如果不包含，则索引应该创建为PRIMARY KEY或UNIQUE索引。对于单列惟一性索引，这保证单列不包含重复的值。对于多列惟一性索引，保证多个值的组合不重复。

PRIMARY KEY索引和UNIQUE索引非常类似。事实上，PRIMARY KEY索引仅是一个具有名称PRIMARY的UNIQUE索引。这表示一个表只能包含一个PRIMARY KEY，因为一个表中不可能具有两个同名的索引。

下面的SQL语句对students表在sid上添加PRIMARY KEY索引。



ALTER TABLE students ADD PRIMARY KEY (sid)



4.  删除索引
可利用ALTER TABLE或DROP INDEX语句来删除索引。类似于CREATE INDEX语句，DROP INDEX可以在ALTER TABLE内部作为一条语句处理，语法如下。



DROP INDEX index_name ON talbe_name

ALTER TABLE table_name DROP INDEX index_name

ALTER TABLE table_name DROP PRIMARY KEY



其中，前两条语句是等价的，删除掉table_name中的索引index_name。

第3条语句只在删除PRIMARY KEY索引时使用，因为一个表只可能有一个PRIMARY KEY索引，因此不需要指定索引名。如果没有创建PRIMARY KEY索引，但表具有一个或多个UNIQUE索引，则MySQL将删除第一个UNIQUE索引。

如果从表中删除了某列，则索引会受到影响。对于多列组合的索引，如果删除其中的某列，则该列也会从索引中删除。如果删除组成索引的所有列，则整个索引将被删除。



5．查看索引

mysql> show index from tblname;

mysql> show keys from tblname;

　　· Table

　　表的名称。

　　· Non_unique

　　如果索引不能包括重复词，则为0。如果可以，则为1。

　　· Key_name

　　索引的名称。

　　· Seq_in_index

　　索引中的列序列号，从1开始。

　　· Column_name

　　列名称。

　　· Collation

　　列以什么方式存储在索引中。在MySQL中，有值‘A’（升序）或NULL（无分类）。

　　· Cardinality

　　索引中唯一值的数目的估计值。通过运行ANALYZE TABLE或myisamchk -a可以更新。基数根据被存储为整数的统计数据来计数，所以即使对于小型表，该值也没有必要是精确的。基数越大，当进行联合时，MySQL使用该索引的机会就越大。

　　· Sub_part

　　如果列只是被部分地编入索引，则为被编入索引的字符的数目。如果整列被编入索引，则为NULL。

　　· Packed

　　指示关键字如何被压缩。如果没有被压缩，则为NULL。

　　· Null

　　如果列含有NULL，则含有YES。如果没有，则该列含有NO。

　　· Index_type

　　用过的索引方法（BTREE, FULLTEXT, HASH, RTREE）。

　　· Comment

6．什么情况下使用索引
       表的主关键字
自动建立唯一索引

如zl_yhjbqk（用户基本情况）中的hbs_bh（户标识编号）

表的字段唯一约束

ORACLE利用索引来保证数据的完整性

如lc_hj（流程环节）中的lc_bh+hj_sx（流程编号+环节顺序）

直接条件查询的字段

在SQL中用于条件约束的字段

如zl_yhjbqk（用户基本情况）中的qc_bh（区册编号）

select * from zl_yhjbqk where qc_bh=’7001’

查询中与其它表关联的字段

字段常常建立了外键关系

如zl_ydcf（用电成份）中的jldb_bh（计量点表编号）

select * from zl_ydcf a,zl_yhdb b where a.jldb_bh=b.jldb_bh and b.jldb_bh=’540100214511’

查询中排序的字段

排序的字段如果通过索引去访问那将大大提高排序速度

select * from zl_yhjbqk order by qc_bh（建立qc_bh索引）

select * from zl_yhjbqk where qc_bh=’7001’ order by cb_sx（建立qc_bh+cb_sx索引，注：只是一个索引，其中包括qc_bh和cb_sx字段）

查询中统计或分组统计的字段
```
select max(hbs_bh) from zl_yhjbqk

select qc_bh,count(*) from zl_yhjbqk group by qc_bh
```


什么情况下应不建或少建索引
```


表记录太少

如果一个表只有5条记录，采用索引去访问记录的话，那首先需访问索引表，再通过索引表访问数据表，一般索引表与数据表不在同一个数据块，这种情况下ORACLE至少要往返读取数据块两次。而不用索引的情况下ORACLE会将所有的数据一次读出，处理速度显然会比用索引快。

如表zl_sybm（使用部门）一般只有几条记录，除了主关键字外对任何一个字段建索引都不会产生性能优化，实际上如果对这个表进行了统计分析后ORACLE也不会用你建的索引，而是自动执行全表访问。如：

select * from zl_sybm where sydw_bh=’5401’（对sydw_bh建立索引不会产生性能优化）

经常插入、删除、修改的表

对一些经常处理的业务表应在查询允许的情况下尽量减少索引，如zl_yhbm，gc_dfss，gc_dfys，gc_fpdy等业务表。

数据重复且分布平均的表字段

假如一个表有10万行记录，有一个字段A只有T和F两种值，且每个值的分布概率大约为50%，那么对这种表A字段建索引一般不会提高数据库的查询速度。

经常和主字段一块查询但主字段索引值比较多的表字段

如gc_dfss（电费实收）表经常按收费序号、户标识编号、抄表日期、电费发生年月、操作 标志来具体查询某一笔收款的情况，如果将所有的字段都建在一个索引里那将会增加数据的修改、插入、删除时间，从实际上分析一笔收款如果按收费序号索引就已 经将记录减少到只有几条，如果再按后面的几个字段索引查询将对性能不产生太大的影响。

对千万级MySQL数据库建立索引的事项及提高性能的手段

一、注意事项：

首先，应当考虑表空间和磁盘空间是否足够。我们知道索引也是一种数据，在建立索引的时候势必也会占用大量表空间。因此在对一大表建立索引的时候首先应当考虑的是空间容量问题。

其次，在对建立索引的时候要对表进行加锁，因此应当注意操作在业务空闲的时候进行。

二、性能调整方面：

首当其冲的考虑因素便是磁盘I/O。物理上，应当尽量把索引与数据分散到不同的磁盘上（不考虑阵列的情况）。逻辑上，数据表空间与索引表空间分开。这是在建索引时应当遵守的基本准则。

其次，我们知道，在建立索引的时候要对表进行全表的扫描工作，因此，应当考虑调大初始化参数db_file_multiblock_read_count的值。一般设置为32或更大。

再次，建立索引除了要进行全表扫描外同时还要对数据进行大量的排序操作，因此，应当调整排序区的大小。

    9i之前，可以在session级别上加大sort_area_size的大小，比如设置为100m或者更大。

    9i以后，如果初始化参数workarea_size_policy的值为TRUE，则排序区从pga_aggregate_target里自动分配获得。

最后，建立索引的时候，可以加上nologging选项。以减少在建立索引过程中产生的大量redo，从而提高执行的速度。

MySql在建立索引优化时需要注意的问题

设计好MySql的索引可以让你的数据库飞起来，大大的提高数据库效率。设计MySql索引的时候有一下几点注意：
1，创建索引

对于查询占主要的应用来说，索引显得尤为重要。很多时候性能问题很简单的就是因为我们忘了添加索引而造成的，或者说没有添加更为有效的索引导致。如果不加

索引的话，那么查找任何哪怕只是一条特定的数据都会进行一次全表扫描，如果一张表的数据量很大而符合条件的结果又很少，那么不加索引会引起致命的性能下

降。但是也不是什么情况都非得建索引不可，比如性别可能就只有两个值，建索引不仅没什么优势，还会影响到更新速度，这被称为过度索引。

2，复合索引

比如有一条语句是这样的：select * from users where area=’beijing’ and age=22;

如果我们是在area和age上分别创建单个索引的话，由于mysql查询每次只能使用一个索引，所以虽然这样已经相对不做索引时全表扫描提高了很多效

率，但是如果在area、age两列上创建复合索引的话将带来更高的效率。如果我们创建了(area, age,

salary)的复合索引，那么其实相当于创建了(area,age,salary)、(area,age)、(area)三个索引，这被称为最佳左前缀

特性。因此我们在创建复合索引时应该将最常用作限制条件的列放在最左边，依次递减。

3，索引不会包含有NULL值的列

只要列中包含有NULL值都将不会被包含在索引中，复合索引中只要有一列含有NULL值，那么这一列对于此复合索引就是无效的。所以我们在数据库设计时不要让字段的默认值为NULL。

4，使用短索引

对串列进行索引，如果可能应该指定一个前缀长度。例如，如果有一个CHAR(255)的 列，如果在前10 个或20 个字符内，多数值是惟一的，那么就不要对整个列进行索引。短索引不仅可以提高查询速度而且可以节省磁盘空间和I/O操作。

5，排序的索引问题

mysql查询只使用一个索引，因此如果where子句中已经使用了索引的话，那么order by中的列是不会使用索引的。因此数据库默认排序可以符合要求的情况下不要使用排序操作；尽量不要包含多个列的排序，如果需要最好给这些列创建复合索引。

6，like语句操作

一般情况下不鼓励使用like操作，如果非使用不可，如何使用也是一个问题。like “%aaa%” 不会使用索引而like “aaa%”可以使用索引。

7，不要在列上进行运算

select * from users where

YEAR(adddate)

8，不使用NOT IN和操作

NOT IN和操作都不会使用索引将进行全表扫描。NOT IN可以NOT EXISTS代替，id3则可使用id>3 or id
```
