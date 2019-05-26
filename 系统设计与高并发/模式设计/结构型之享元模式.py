#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 0:16
# @Author  : liuhu
# @Site    : 
# @File    : 结构型之享元模式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
from enum import Enum
import random

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


# print(TreeType.apple_tree.value)
# print(TreeType.cherry_tree.value)

class Tree:
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            print('{0}不存在'.format(tree_type))
            # obj = object.__new__(cls)
            # cls.pool[tree_type] = obj
            obj = super(Tree, cls).__new__(cls)
            cls.pool[tree_type] = obj
            print(cls.pool)
            obj.tree_type = tree_type
        else:
            print('{0}已存在'.format(tree_type))
        return obj

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type,
                                                                       age, x, y))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30  # 单位为年
    min_point, max_point = 0, 100
    tree_counter = 0
    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1
    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1
    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    print('trees rendered: {}'.format(tree_counter))
    print('trees actually created: {}'.format(len(Tree.pool)))
    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))
    print('{} == {}? {}'.format(id(t5), id(t6), id(t5) == id(t6)))


if __name__ == '__main__':
    main()
