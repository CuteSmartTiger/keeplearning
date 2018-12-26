#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 14:50
# @Author  : liuhu
# @Site    : 
# @File    : unittest_test.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import unittest

# 本章主要是介绍unittest的简单使用
class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('类执行前的方法')

    @classmethod
    def tearDownClass(cls):
        print('类执行之后的方法')

    def setUp(self):
        print('方法之前')

    def tearDown(self):
        print('方法之后')

    @unittest.skip('test_01')
    def test_01(self):
        print('测试案例1')

    def test_02(self):
        print('测试案例2')


if __name__ =="__main__":
    unittest.main()

    # 用容器的方式启动测试
    # suite = unittest.TestSuite()
    # suite.addTest(TestMethod('test_01'))
    # suite.addTest(TestMethod('test_02'))
    # unittest.TextTestRunner().run(suite)
