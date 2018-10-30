####概念
- 14.1
    - 序列可以迭代的原因
    - 鸭子类型(duck typing)
    - 白鹅类型(goose-typing) 
    - 判断可迭代的两种方法： issubclass (Sentence, abc.Iterable)
    
- 14.2 
    - 可迭代的对象
    - 如何实现迭代器
    - 使用 iter(...) 函数构建迭代器，以及如何使用 next(...) 函
数使用迭代器
    - 
- 14.3
    - 可迭代的对象一定不能是自身的迭代器。也就是说，可迭代的对象必须实现 __iter__ 方法，但不能实现 __next__ 方法。



- 14.10
    - 生成器函数的定义
    - yield from 底层的原理


- 14.11
    - 可迭代的规约函数：函数可接受一个可迭代的对象，然后返回单个结果。这些函数叫“归约”函数

##### 内置底层方法集：
__getitem__

__iter__

__next__


__init__:
__init__ 更应该称为初始化方法，因为它并不会构建实例，而是初始化通过 self 参数传入的实例。

__new__:
实例其实是由 __new__ 方法构建的。参见构造方法词条。

##### 内置模块：
re
reprlib

- 14.8
    - itertools
        - count()
        - takewhile()


- 14.9 标准库中的生成器函数
    - 内置的：
        - reversed
        从后向前，倒序产出 seq 中的元素；seq 必须是序列，或者是实现了 __reversed__ 特殊方法的对象
        
        - filter(predicate, it)
        把 it 中的各个元素传给 predicate，如果predicate(item) 返回真值，那么产出对应的元素；如果 predicate 是 None，那么只产出真值元素
        
        - enumerate(iterable,start=0)
        产出由两个元素组成的元组，结构是 (index,item)，其中 index 从 start 开始计数，item 则从iterable 中获取
        
        - map(func, it1,[it2, ..., itN])
        把 it 中的各个元素传给func，产出结果；如果传入N 个可迭代的对象，那么 func 必须能接受 N 个参数，而且要并行处理各个可迭代的对象
        
        - zip(it1, ..., itN)
        并行从输入的各个可迭代对象中获取元素，产出由 N 个元素组成的元组，只要有一个可迭代的对象到头了，就默默地停止
        
    
    - itertools模块中的
    
    
    
- 14.10 yield from




- 14.15
    - 迭代器与生成器之间的关系
        - 实现方式：生成器这种 Python 语言结构可以使用两种方式编写：含有 yield 关键字的函数，或者生成
        器表达式。调用生成器函数或者执行生成器表达式得到的生成器对象属于语言内部的 GeneratorType 类型
    
        - 接口：Python 的迭代器协议定义了两个方法：__next__ 和 __iter__。生成器对象实现了这两个方法，
        因此从这方面来看，所有生成器都是迭代器
        
        
        
