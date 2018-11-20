流水线


redis的命令时间是微妙级
pipeline每次条数要控制（网络）

客户端实现


与M操作的对比：
m命令为原子的
pipeline是进行过拆分的


#### 建议
1. 注意pipeline携带数量
2. pipeline每次只能作用在一个redis节点上
3. M操作与pipeline的区别
