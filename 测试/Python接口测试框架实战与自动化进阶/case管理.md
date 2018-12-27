globals()['userid'] = 9999

assertEqual

按定义函数的字母顺序排序执行

skip()方法跳过测试案例


#### 启动测试的方法
- main()方式运行测试
```PYTHON
unittest.main()
```

- 用容器的方式启动测试
```PYTHON
suite = unittest.TestSuite()
suite.addTest(TestMethod('test_01'))
suite.addTest(TestMethod('test_02'))
unittest.TextTestRunner().run(suite)
```

#### 疑问
1. 如何将不同py文件的测试导入case里
