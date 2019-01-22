两台虚拟机设备

本机域名解析：
vim /etc/hosts
192.168.17.129 elk-node1
192.168.17.131 elk-node2


检查域名解析情况
ping elk-node1

scp /etc/hosts 192.168.37.134:/etc/
或者直接用文件复制



[elasticsearch官方安装步骤](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html)

需要先安装Java，
- [Ubuntu 18.04 安装java8](https://www.cnblogs.com/phpper/p/9201562.html)
- 编写Java安装的shell脚本
  ```shell
  # 添加ppa
  sudo add-apt-repository ppa:webupd8team/java
  sudo apt-get update

  # 安装oracle-java-installer
  sudo apt-get install -y  oracle-java8-installer

  # 设置系统默认jdk
  sudo update-java-alternatives -s java-8-oracle
  ```

  查看Java是否安装成功
  java -version

mater-slave模式非高可用模式  

- 创建elasticsearch data的存放目录，并修改该目录的属主属组
    ```
     mkdir -p /data/es-data   (自定义用于存放收集的data数据的目录)
     chown -R elasticsearch:elasticsearch /data/es-data （修改该目录的属主属组，必须，否则收集时无法写入数据）
    ```
- 修改elasticsearch的配置文件 （记住去除每行前的空格）
    ```shell
    # vim /etc/elasticsearch/elasticsearch.yml

    找到配置文件中的cluster.name，打开该配置并设置集群名称
    cluster.name: my-application(自定义，同一个集群的名字一样)

    找到配置文件中的node.name，打开该配置并设置节点名称
    node.name: elk-node1

    修改data存放的路径
    path.data: /data/es-data

    修改elasticsearch本身logs日志的路径，与上面收集的日志我们叫数据，以作区分
    path.logs: /var/log/elasticsearch/

    配置内存使用用交换分区，锁住内存，不被使用到交
    换分区去（通常在内存不足时，休眠的程序内存信息会交换到交换分区）
    bootstrap.memory_lock: true

    监听的网络地址
    network.host: 0.0.0.0

    开启监听的端口
    http.port: 9200

    # 增加新的参数，这样head插件可以访问es (5.x版本，如果没有可以自己手动加)
    http.cors.enabled: true
    http.cors.allow-origin: "*"

    #副服务器要开启
    discovery.zen.ping.multicast.enabled:false   #关闭多播
    discovery.zen.ping.unicast.hosts:["",""] #主服务器与自己的地址


    ```
-    启动elasticsearch服务
systemctl start elasticsearch.service
systemctl enable elasticsearch.service
systemctl restart elasticsearch.service

systemctl status elasticsearch.service


/etc/init.d/elasticsearch start


/etc/systemd/system.conf


创建开机自启动服务
# chkconfig elasticsearch on

- 通过浏览器请求下9200的端口，看下是否成功
    ```
    查看端口
    netstat -anpt | grep 9200



    浏览器访问测试是否正常（以下为正常）
      # curl http://127.0.0.1:9200/
      {
        "name" : "linux-node1",
        "cluster_name" : "demon",
        "cluster_uuid" : "kM0GMFrsQ8K_cl5Fn7BF-g",
        "version" : {
          "number" : "5.4.0",
          "build_hash" : "780f8c4",
          "build_date" : "2017-04-28T17:43:27.229Z",
          "build_snapshot" : false,
          "lucene_version" : "6.5.0"
        },
        "tagline" : "You Know, for Search"
      }

      第二种方法，通过API查看
      利用API查看状态
      # curl -i -XGET 'localhost:9200/_count?pretty' -d '{"query":{"natch_all":{}}}'

      #出现以下结果
      HTTP/1.1 200 OK
      content-type: application/json; charset=UTF-8
      content-length: 95

      {
        "count" : 0,
        "_shards" : {
          "total" : 0,
          "successful" : 0,
          "failed" : 0
        }
      }

    ```
##### 插件件的安装

- 安装elasticsearch-head插件
```
安装docker镜像或者通过github下载elasticsearch-head项目都是可以的，1或者2两种方式选择一种安装使用即可

1. 使用docker的集成好的elasticsearch-head
    # docker run -p 9100:9100 mobz/elasticsearch-head:5

    docker容器下载成功并启动以后，运行浏览器打开http://localhost:9100/

2. 使用git安装elasticsearch-head
    # yum install -y npm
    # git clone git://github.com/mobz/elasticsearch-head.git
    # cd elasticsearch-head
    # npm install
    # npm run start
    检查端口是否起来
    netstat -antp |grep 9100
    浏览器访问测试是否正常
    http://IP:9100/

在/usr/share/elasticsearch/bin/elasticsearch-head目录下重启 npm run 可以重启head



以下失效
# 装插件来看
/usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head

chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/plugins

systemctl restart elasticsearch


# 装插件来进行集群的管理
/usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-kopf #用来管理

chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/plugins

systemctl restart elasticsearch



查看插件
http://ip:9200/_plugin/head/
http://ip:9200/_plugin/kopf/
出现页面
```


#### 参考文章
- [快速搭建ELK日志分析系统](https://www.cnblogs.com/yuhuLin/p/7018858.html)
