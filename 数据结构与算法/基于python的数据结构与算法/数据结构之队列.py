#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 16:40
# @Author  : liuhu
# @File    : 数据结构之队列.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
# !/usr/bin/env python
# -*- coding: utf-8 -*-


# 队列ADT（抽象数据类型）一般提供以下接口：
#
# ① Queue() 创建队列
# ② enqueue(item) 向队尾插入项
# ③ dequeue() 返回队首的项，并从队列中删除该项
# ④ empty() 判断队列是否为空
# ⑤ size() 返回队列中项的个数


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

# 参与者围成一个圆圈，从某个人（队首）开始报
# 数，报数到n+1的人退出圆圈，然后从退出人的下
# 一位重新开始报数；重复以上动作，直到只剩下一个人为止。
def josephus(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        print(simqueue.dequeue())
    return simqueue.dequeue()


if __name__ == '__main__':
    print(josephus(["Bill", "David", "Kent", "Jane", "Susan", "Brad"], 3))
