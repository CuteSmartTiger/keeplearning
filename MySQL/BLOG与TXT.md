- MySQL中TEXT与BLOB字段类型的区别
```
一、类型。
BLOB是一个二进制大对象，可以容纳可变数量的数据。有4种 BLOB类型：TINYBLOB、BLOB、MEDIUMBLOB和LONGBLOB。它们只是可容纳值的最大长度不同。 有4种TEXT类型：TINYTEXT、TEXT、MEDIUMTEXT和LONGTEXT。这些对应4种BLOB类型，有相同的最大长度和存储需求。

二、类型区别。

BLOB是一个二进制大对象，可以容纳可变数量的数据。有4种BLOB类型：TINYBLOB、BLOB、MEDIUMBLOB和LONGBLOB。它们只是可容纳值的最大长度不同。

有4种TEXT类型：TINYTEXT、TEXT、MEDIUMTEXT和LONGTEXT。这些对应4种BLOB类型，有相同的最大长度和存储需求。

三、 字符集、大小写。

BLOB 列被视为二进制字符串(字节字符串)。TEXT列被视为非二进制字符串(字符字符串)。BLOB列没有字符集，并且排序和比较基于列值字节的数值值。TEXT列有一个字符集，并且根据字符集的 校对规则对值进行排序和比较。

在TEXT或BLOB列的存储或检索过程中，不存在大小写转换。

四、 严格模式。

当未运行在严格模式时，如果你为BLOB或TEXT列分配一个超过该列类型的最大长度的值值，值被截取以保证适合。如果截掉的字符不是空格，将会产生一条警告。使用严格SQL模式，会产生错误，并且值将被拒绝而不是截取并给出警告。

五、

在大多数方面，可以将BLOB列视为能够足够大的VARBINARY列。同样，可以将TEXT列视为VARCHAR列。BLOB和TEXT在以下几个方面不同于VARBINARY和VARCHAR：

 ·         当保存或检索BLOB和TEXT列的值时不删除尾部空格。(这与VARBINARY和VARCHAR列相同）。

 请注意比较时将用空格对TEXT进行扩充以适合比较的对象，正如CHAR和VARCHAR。

 ·         对于BLOB和TEXT列的索引，必须指定索引前缀的长度。对于CHAR和VARCHAR，前缀长度是可选的。

 ·         BLOB和TEXT列不能有 默认值。

 LONG和LONG VARCHAR对应MEDIUMTEXT数据类型。这是为了保证兼容性。如果TEXT列类型使用BINARY属性，将为列分配列字符集的二元 校对规则。

 MySQL连接程序/ODBC将BLOB值定义为LONGVARBINARY，将TEXT值定义为LONGVARCHAR。

 由于BLOB和TEXT值可能会非常长，使用它们时可能遇到一些约束：

 ·         当排序时只使用该列的前max_sort_length个字节。max_sort_length的 默认值是1024；该值可以在启动d服务器时使用--max_sort_length选项进行更改。

 运行时增加max_sort_length的值可以在排序或组合时使更多的字节有意义。任何客户端可以更改其会话max_sort_length变量的值：

 ```
