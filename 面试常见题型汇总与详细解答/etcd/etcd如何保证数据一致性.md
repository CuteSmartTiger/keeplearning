#### 节点角色
- 集群总每个节点都有三种可能的角色：
  - leader：对客户端通信的入口，对内数据同步的发起者，一个集群通常只有一个leader节点
  - follower:非leader的节点，被动的接受来自leader的数据请求
  - candidate:一种临时的角色，只存在于leader的选举阶段，某个节点想要变成leader，那么就发起投票请求，同时自己变成candidate。如果选举成功，则变为candidate，否则退回为follower


#### 数据提交的过程
- 第一阶段：eader扮演的是分布式事务中的协调者，每次有数据更新的时候产生二阶段提交（two-phase commit）。在leader收到数据操作的请求，先不着急更新本地数据（数据是持久化在磁盘上的），而是生成对应的log，然后把生成log的请求广播给所有的follower。
每个follower在收到请求之后有两种选择：一种是听从leader的命令，也写入log，然后返回success回去；另一种情况，在某些条件不满足的情况下，follower认为不应该听从leader的命令，返回false；然后回到leader，此时如果超过半数的follower都成功写了log，那么leader开始第二阶段的提交
- 第二阶段：正式写入数据，然后同样广播给follower，follower也根据自身情况选择写入或者不写入并返回结果给leader。继续上面的例子，leader先写自己的数据，然后告诉follower也开始持久化数据，这两阶段中如果任意一个都有超过半数的follower返回false或者根本没有返回，那么这个分布式事务是不成功的。



#### 选举
- 初始状态下，大家都是平等的follower，每个follower内部都维护了一个随机的timer，在timer时间到了的时候还没有人主动联系它的话，那它就要变成candidate，同时发出投票请求（RequestVote）给其他人
- 每个follower一轮只能投一次票给一个candidate，对于相同条件的candidate，follower们采取先来先投票的策略。如果超过半数的follower都认为他是合适做领导的，那么恭喜，新的leader产生了
- 选举完成后，leader定时发送心跳检测(heart beat)，follower是通过心跳来感知leader的存在的，如果在timer期间内没有收leader的联络，这时很可能leader已经跪了，follower又开始蠢蠢欲动，新的一轮(term)选举开始了




#### 选举遇到的问题
