#### [MySQL半同步复制(Semisynchronous replication)原理与配置详解](https://www.linuxidc.com/Linux/2018-04/151922.htm)
- MySQL5.7版本的半同步原理
  - AFTER_COMMIT（5.5，5.6默认值）
    - master将每个事务写入binlog之后，先提交事务，然后将binlog数据传递到slave并刷新到磁盘(relay log)。接着master等待slave反馈收到relay log，只有收到ack之后master才将commit OK结果反馈给客户端。

  - AFTER_SYNC（5.7默认值）
    - master将每个事务写入binlog，然后将binlog数据传递到slave并刷新到磁盘(relay log)。master等待slave反馈接收到relay log的ack之后，再提交事务并且返回commit OK结果给客户端。即使主库crash了，所有在主库上已经提交的事务都能保证已经同步到slave的relay log中。如图二所示。
  - 解决的问题：MySQL5.7的半同步复制引入after_sync模式，主要是解决了after_commit导致的主库crash后主从之间数据不一致的问题。在引入after_sync模式后，所有提交的数据都已经被复制，故障切换时数据一致性将得到提升。（另外，在5.7版本的semi sync框架中，独立出一个ack collector thread，专门用于接收slave的反馈信息。这样master上有两个线程独立工作，可以同时发送binlog到slave，和接收slave的反馈）


#### 异步复制（Asynchronous replication）
MySQL默认的复制是异步的，主库在执行完客户端提交的事务后会立即将结果返给给客户端，并不关心从库是否已经接收并处理。原理最简单，性能最好，但是主从之间数据不一致的概率很大。

#### 全同步复制（Fully synchronous replication）
指当主库执行完一个事务，所有的从库都执行了该事务才返回给客户端。因为需要等待所有从库执行完该事务才能返回，所以全同步复制的性能必然会收到严重的影响




- [半同步复制](https://www.cnblogs.com/zero-gg/p/9057092.html)
