可以看到redis-trib.rb具有以下功能：

1、 create ：创建集群
2、 check ：检查集群
3、 info ：查看集群信息
4、 fix ：修复集群
5、 reshard ：在线迁移slot
6、 rebalance ：平衡集群节点slot数量
7、 add-node ：将新节点加入集群
8、 del-node ：从集群中删除节点
9、 set-timeout ：设置集群节点间心跳连接的超时时间
10、 call ：在集群全部节点上执行命令
11、 import ：将外部redis数据导入集群

redis-trib.rb主要有两个类： ClusterNode 和 RedisTrib 。 ClusterNode 保存了每个节点的信息， RedisTrib 则是redis-trib.rb各个功能的实现
