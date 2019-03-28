针对每一种设计模式，将从以下方面进行理解：

1. 模型的含义
2. 他的出现解决什么问题
3. 他的优缺点
4. 设计思路，使用场景，代码示例
5. 设计模式的原则
6. 常用的重要的设计模式有哪些

设计模式的原则
1. 开放/封闭原则（open/close
principle）是面向对象设计的基本原则之一（SOLID中的O）


[第一章 创建型模式](#build)
----
- [2.1 工厂模式](#)(重点)
- [2.2 建造者模式](#)
- [2.3 原型模式](#)

[第二章 结构型模式](#construct)
----
- [2.1 适配器模型](#adopt)
- [2.2 修饰器模型](#decorator)(重点)

- [2.5 MVC模型](#mvc)(重点)
- [2.6 代理设计模式（Proxy design pattern）](#Proxy)
    - 保护/防护代理:用于对处理敏感信息的对象进行访问控制
    - 远程代理：代表一个活跃于远程位置（例如，我们自己的远程服务器或云服务）的对象
    - 虚拟代理：将一个对象的初始化延迟到真正需要使用时进行
    - 智能（引用）代理：通过添加帮助信息（比如，引用计数）来扩展一个对象的行为时，可以使用智能（引用）代理


[第三章 行为型模式](#motion)
----
- [3.1 责任链模式](#Chain)
- [3.2 命令模式](#Command)
- [3.3 解释器模式](#Interpreter)
- [3.4 观察者模式](#inspect)(重点)
- [3.5 状态模式](#State)
- [3.6 策略模式](#Strategy)
- [3.7 模板模式](#template)





####  结构型模式
<h5 id='construct'></h>



- <h5 id='mvc'>MVC模型</h>

  - 概念：模型-视图-控制器


 <h5 id='Proxy'>代理设计模式</h>  

  - 概念
  - 设计思路：
  - 实例
    - 1
    - 2
    - 3

#### 行为型模式
<h5 id='motion'></h>

<h5 id='inspect'>3.4 观察者模式</h>

  - 使用的场景：
  - 主要设计思路：
  - 代码示例：
    ```python
    class Publisher:
        def __init__(self):
            self.observers = []

        def add(self, observer):
            if observer not in self.observers:
                self.observers.append(observer)
            else:
                print('Failed to add: {}'.format(observer))

        def remove(self, observer):
            try:
                self.observers.remove(observer)
            except ValueError:
                print('Failed to remove: {}'.format(observer))

        def notify(self):
            print('notify')
            [o.notify(self) for o in self.observers]


    class DefaultFormatter(Publisher):
        def __init__(self, name):
            Publisher.__init__(self)
            self.name = name
            self._data = 0

        def __str__(self):
            return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, new_value):
            try:
                self._data = int(new_value)
            except ValueError as e:
                print('Error: {}'.format(e))
            else:
                self.notify()


    class HexFormatter:
        def notify(self, publisher):
            print("{}: '{}' has now hex data = {}".format(type(self).__name__, publisher.name, hex(publisher.data)))


    class BinaryFormatter:
        def notify(self, publisher):
            print("{}: '{}' has now bin data = {}".format(type(self).__name__, publisher.name, bin(publisher.data)))


    def main():
        df = DefaultFormatter('test1')
        print(df)
        print('==========================')
        hf = HexFormatter()
        df.add(hf)
        hf2 = HexFormatter()
        df.add(hf2)
        df.data = 3


        # df.data = 5
        # print(df.observers)
        # print('==========================')
        # bf = BinaryFormatter()
        # df.add(bf)
        # df.data = 21
        # print(df)
        # print('==========================')
        # df.remove(hf)
        # df.data = 40
        # print(df)
        # print('==========================')
        # df.remove(hf)
        # df.add(bf)
        # df.data = 'hello'
        # print(df)
        # print('==========================')
        # df.data = 15.8
        # print(df)


    if __name__ == '__main__':
        main()
    ```




<h5 id='State'>3.5 状态模式</h>





<h5 id='Strategy'>3.6 策略模式</h>

  - 使用的场景示例：
    1. 使用百度去机场有不同的路线，基于不同的需求考量提供不同的路线

  - 主要的设计思路：
    1. 使用多种算法来解决一个问题，其杀手级特性是能够在运行时透明地切换算法（客户端代码对变化无感知）
  - 对比进行更好的理解：与工厂模式(工厂方法与抽象工厂)进行对比
  - 不同的字符长度，通过不同的算法策略返回是否字母单一，代码示例
    ```PYTHON
    import time

    SLOW = 3  # 单位为秒
    LIMIT = 5  # 字符数
    WARNING = 'too bad, you picked the slow algorithm :('


    def pairs(seq):
        n = len(seq)
        for i in range(n):
            yield seq[i], seq[(i + 1) % n]


    def allUniqueSort(s):
        if len(s) > LIMIT:
            print(WARNING)
            time.sleep(SLOW)
        srtStr = sorted(s)
        for (c1, c2) in pairs(srtStr):
            if c1 == c2:
                return False
        return True


    def allUniqueSet(s):
        if len(s) < LIMIT:
            print(WARNING)
        time.sleep(SLOW)
        return True if len(set(s)) == len(s) else False


    def allUnique(s, strategy):
        return strategy(s)


    def main():
        while True:
            word = None
            while not word:
                word = input('Insert word (type quit to exit)> ')
                if word == 'quit':
                    print('bye')
                    return
                strategy_picked = None
                strategies = {'1': allUniqueSet, '2': allUniqueSort}
                while strategy_picked not in strategies.keys():
                    strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort andpair> ')
                    try:
                        strategy = strategies[strategy_picked]
                        print('allUnique({}): {}'.format(word, allUnique(word,
                                                                         strategy)))
                    except KeyError as err:
                        print('Incorrect option: {}'.format(strategy_picked))
                        print()

        if __name__ == '__main__':
            main()
    ```
