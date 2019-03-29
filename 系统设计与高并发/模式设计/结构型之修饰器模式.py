#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 14:50
# @Author  : liuhu
# @File    : 结构型之修饰器模式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# def fibonacci(n):
#     assert (n >= 0), 'n must be >= 0'
#     return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)
#
#
# if __name__ == '__main__':
#     from timeit import Timer
#
#     t = Timer('fibonacci(8)', 'from __main__ import fibonacci')
#     print(t.timeit())  # 19.1498459


# known = {0: 0, 1: 1}
#
#
# def fibonacci(n):
#     assert (n >= 0), 'n must be >= 0'
#     if n in known:
#         return known[n]
#     res = fibonacci(n - 1) + fibonacci(n - 2)
#     known[n] = res
#     return res

#
# if __name__ == '__main__':
#     from timeit import Timer
#
#     t = Timer('fibonacci(100)', 'from __main__ import fibonacci')
#     print(t.timeit())  # 0.4535593


import functools


def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer


# @memoize
# def nsum(n):
#     '''返回前n个数字的和'''
#     assert (n >= 0), 'n must be >= 0'
#     return 0 if n == 0 else n + nsum(n - 1)


@memoize
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    from timeit import Timer

    measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci','func': fibonacci}]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time:{}'.format(m['func'].__name__, m['func'].__doc__, m['exec'],
                                                                 t.timeit()))
    # name: fibonacci, doc: 返回斐波那契数列的第n个数, executing: fibonacci(100), time:0.4526535