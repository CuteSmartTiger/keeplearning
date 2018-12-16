##### 基准测试与压力测试的区别
基准测试：简单




##### 基准测试的类型

针对系统的基准测试

针对软件的基准测试



##### mysql基准测试的常见指标
1. TPS 事物数
2. QPS 查询数
3. 响应时间
4. 并发量：同时处理的查询请求数量 （注意与web的并发区别）



##### 计划与设计基准测试
设计
测试数据收集的脚本



注意事项：
只使用部分数据，应使用数据库全部数据
只做了单用户的测试，多用户使用多线程
单服务器上测试分布式应用 推荐使用相同测试架构
反复执行同一查询，太过单一


##### 基准测试工具之mysqlslap（比较简单的工具）
查看是否安装
mysqlslap --help







##### 基准测试工具之sysbench（常用）
- 文件系统I/O性能测试

产看最大内存
free -m


查看磁盘空间
df -lh

文件需要比内存大,准备测试文件
sysbench --test=fileio --file-total-size=1G prepare

查看文测试的参数
sysbench --test=fileio help

sysbench --test=fileio --num-threads=8 --init-rng=on --file-total-size=1G --file-test-mode=rndrw --report-interval=1 run



- CPU 性能测试
sysbench --test=cpu --cpu-max-prime=10000 run


- 内存性能测试



- Oltp测试需要执行具体的lua脚本
