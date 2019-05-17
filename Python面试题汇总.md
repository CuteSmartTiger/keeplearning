#### 基础概念
- 鸭子类型

- monkey patch

- 自省


- is 与 == 的区别

- 列表或者字典推导式

- GIL解释器锁

- 不可重复的数据结构

- 判断对象是否存在属性或者方法

- 单例模式  了解 super指定起始查找点，顺着MRO查找第二个参数  new拦截类的实例化  init创建实例后初始化值   call实现可调用

- 函数式编程
  - map
  - filter
  - reduce
  - 闭包
    - 绑定外部作用域的变量的函数
    - 即使程序离开外部作用域，如果闭包仍然可见，绑定变量不会销毁
    - 每次运行外部函数都会重新创建闭包



#### 数据结构与算法
- 二分查找
- 哈希查找
- 分块查找
- 顺序查找

- 顺序排序
- 插入排序
- 冒泡排序
- shell排序
- 快速排序
- 基数排序
- 二路并归排序



#### Linux
- 常用命令
  - 帮助
    man  tar
    tar --help
    tldr

```SHELL
chown chmod chgrp
ls/rm/cd/cp/mv/touch/rename/ln(软连接与硬链接)
lcate find grep
find . -name '*.pyc' -delete
```

vi/nano
cat/head/tail
more/less


进程相关

ps
kill  执行的原理   发送信号


top/htop


内存
free


网络工具
ifconfig
lsof/netstat 查看端口
ssh/scp    tcpdump抓包


useradd/usermod
groupadd/groupmod




#### 线程  进程  并发  并行  协程  线程安全


- 线程安全  
  - GIL解释器锁
  - 线程同步  如何保证线程同步
    - 互斥索
    - 信号量 参数value为1
    - 事件信号


- 进程间的通信
  - 管道pipe
  - 信号
  - 消息队列
  - 共享内存
  - 信号量
  - socket：web应用这种方式




- 多线程使用


- 多进程使用
  - uwsgi


#### 内存管理
- 分页地址
- 分段机制
- 虚拟内存
- 垃圾回收
  - 引用计算为主  标记清除和分代回收为辅  解决循环引用

#### 网络编程
- 网络协议TCP和UDP
  - 浏览器输入一个url中间经历的过程:
    1. DNS查询
    2. TCP握手      wireshark抓包更直观 重点有两点(状态与发包内容)  手画图  为什么是三次握手而不是两次或者四次
    3. HTTP请求     
    4. 反向代理
    5. uwsgi        
    6. web app   （flask框架）
    7. TCP挥手    为什么是四次而不是三次或者五次
  - TCP与UDP的区别
    - 面向连接  可靠地  基于字节流
    - 无连接  不可靠   面向报文


- HTTP协议
  - pip install httpie  
  - curl
  - HTTP协议有哪些部分组成  使用抓包工具去查看和理解
    - HTTP请求
      - 状态行
      - 请求头
      - 消息主体
    - HTTP响应
      - 状态行
      - 响应头
      - 响应正文
    - HTTP响应状态码  五中类型
  - 幂等性  GET
  - 长连接
    - 为什么需要长连接
    - 如何区分短还是长连接
      - 1. content-Length 携带报文长度
      - 2. Transfer-Encoding:chunked
  - cookie与session的区别，识别用户
  - 前后端分离如何识别用户状态
  - 本节重点内容：
    - 请求和响应的组成
    - 常用HTTP方法和幂等性
    - 长连接 session  cookie

- socket编程原理
  - TCP编程


- 并发编程IO多路复用


- 并发网络库


- 异步框架


#### 设计模式
- 装饰器模式
- 观察着模式
- 单例模式
- 工厂方法
- 抽象工厂
- 代理模式
