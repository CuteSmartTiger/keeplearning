在学习使用ab命令之前，首先要了解压力测试的几个概念：（自己可以上网查下具体的概念）

吞吐率（Requests per second）
概念：服务器并发处理能力的量化描述，单位是reqs/s，指的是某个并发用户数下单位时间内处理的请求数。某个并发用户数下单位时间内能处理的最大请求数，称之为最大吞吐率。
计算公式：总请求数 / 处理完成这些请求数所花费的时间，即
Request per second = Complete requests / Time taken for tests

并发连接数（The number of concurrent connections）
概念：某个时刻服务器所接受的请求数目，简单的讲，就是一个会话。

并发用户数（The number of concurrent users，Concurrency Level）
概念：要注意区分这个概念和并发连接数之间的区别，一个用户可能同时会产生多个会话，也即连接数。

用户平均请求等待时间（Time per request）
计算公式：处理完成所有请求数所花费的时间/ （总请求数 / 并发用户数），即
Time per request = Time taken for tests /（ Complete requests / Concurrency Level）

服务器平均请求等待时间（Time per request: across all concurrent requests）
计算公式：处理完成所有请求数所花费的时间 / 总请求数，即
Time taken for / testsComplete requests
可以看到，它是吞吐率的倒数。
同时，它也=用户平均请求等待时间/并发用户数，即
Time per request / Concurrency Level

3.ab工具的介绍

ab是apache自带的压力测试工具。ab非常实用，它不仅可以对apache服务器进行网站访问压力测试，也可以对或其它类型的服务器进行压力测试。比如nginx、tomcat、IIS等。
 安装：
1.公司应该有程序员吧，可以安装一个wamp或者phpstudy，这样apache服务器和mysql数据库都有了，一举多得

         
文件位置：打开你安装的apache的位置：找到 bin文件夹下面的ab.exe
在该文件夹下打开命令行，输入 ab.exe -help

对上面的Options做下解释吧：
-n即requests，用于指定压力测试总共的执行次数。
-c即concurrency，用于指定压力测试的并发数。
-t即timelimit，等待响应的最大时间(单位：秒)。
-b即windowsize，TCP发送/接收的缓冲大小(单位：字节)。
-p即postfile，发送POST请求时需要上传的文件，此外还必须设置-T参数。
-u即putfile，发送PUT请求时需要上传的文件，此外还必须设置-T参数。
-T即content-type，用于设置Content-Type请求头信息，例如：application/x-www-form-urlencoded，默认值为text/plain。
-v即verbosity，指定打印帮助信息的冗余级别。
-w以HTML表格形式打印结果。
-i使用HEAD请求代替GET请求。
-x插入字符串作为table标签的属性。
-y插入字符串作为tr标签的属性。
-z插入字符串作为td标签的属性。
-C添加cookie信息，例如："Apache=1234"(可以重复该参数选项以添加多个)。
-H添加任意的请求头，例如："Accept-Encoding: gzip"，请求头将会添加在现有的多个请求头之后(可以重复该参数选项以添加多个)。
-A添加一个基本的网络认证信息，用户名和密码之间用英文冒号隔开。
-P添加一个基本的代理认证信息，用户名和密码之间用英文冒号隔开。
-X指定使用的代理服务器和端口号，例如:"126.10.10.3:88"。
-V打印版本号并退出。
-k使用HTTP的KeepAlive特性。
-d不显示百分比。
-S不显示预估和警告信息。
-g输出结果信息到gnuplot格式的文件中。
-e输出结果信息到CSV格式的文件中。
-r指定接收到错误信息时不退出程序。
-h显示用法信息，其实就是ab -help。

4.实际测试：


5.分析上面的压测结果：

Server Software: Apache/2.2.25 (服务器软件名称及版本信息)

Server Hostname: www.xxx.com(服务器主机名)

Server Port: 80 (服务器端口)

Document Path: /lol (供测试的URL路径)

Document Length: 0 bytes (供测试的URL返回的文档大小)



Concurrency Level: 100 (并发数)

Time taken for tests: 0.800 seconds (压力测试消耗的总时间)

Complete requests: 100 (压力测试的的总次数)

Failed requests: 0 (失败的请求数)

Total transferred: 16342 bytes (传输的总数据量)

HTML transferred: 0 bytes (HTML文档的总数据量)

Requests per second: 125.03 [#/sec] (mean) (平均每秒的请求数)

Time per request: 799.805 [ms] (mean) (所有并发用户(这里是100)都请求一次的平均时间)

Time per request: 7.998 [ms] (mean, across all concurrent requests) (单个用户请求一次的平均时间)

Transfer rate: 19.95 [Kbytes/sec] received (传输速率，单位：KB/s)
