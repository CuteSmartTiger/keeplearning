第一题：

下面显示了当前 PPIO 测试链上每个钱包地址所包含的余额数排行榜信息（数据为测试数据，仅供参考），如下所示：




A total of 100000 accounts found                              上一页  < 1/200  >下一页

Rank     Address                                                           Balance                     TxCount

1          ppio1SDKRLjDALmN7kV874JLhZAv4Q9TKVhrhg      30000 PPCoin           2000

2          ppio1ZoKAKZftwkdAVXSuPnz2TLJp14pSfhvMj          29990 PPCoin           1999

3          ppio1Yd4y3cYYZZ3pZqxnmn6xydrE4VmvWiX3d       29980 PPCoin            1998

...

如果上面所示的排行榜数据都是放在 redis 数据库中维护的，为了实现以上功能，需要用到 redis 的哪些数据结构及相应的方法？


提示有以下几个功能点：

1. 获取当前排行榜中的总地址（Address）数。

2. 分页获取当前排行榜数据（根据余额数倒序排序）。包含 Rank（名次）、Address（钱包地址）、Balance（余额）、 TxCount（参与事务的总数）。

请给出详细的设计文档。

文档内容示例：需要使用 String 数据结构来存储各个钱包地址的余额信息，键名为：PPIO:Wallet:ppio1SDKRLjDALmN7kV874JLhZAv4Q9TKVhrhg，键值为该账户的余额。通过  GET PPIO:Wallet:ppio1SDKRLjDALmN7kV874JLhZAv4Q9TKVhrhg 来获取账户  ppio1SDKRLjDALmN7kV874JLhZAv4Q9TKVhrhg 的余额信息 ...

答案：
1. 需要用的到的数据结构为：SortSet和Hash,SortSet用于做分页排序，Hash用于存储具体的键值对数据
2. SortSet中使用Address和Balance分别作为set的member和score，存储使用r.zadd('ppio',addrress,score)
，r.zcard('ppio')获取总数量，r.zrevrange(name="ppio",start=(page-1)×10, end=(page-1)×10+perPage)获取第几页的信息
3. Hash中以Address为键，然后存储Address Balance TxCount 对应的信息，r.hkey('ppioinfo',Address,Address_info,Balance,Balance_info, TxCount,TxCountinfo)




参考文章：
1. https://blog.csdn.net/jack85986370/article/details/51483872/
2. https://www.cnblogs.com/xuchunlin/p/7097255.html
