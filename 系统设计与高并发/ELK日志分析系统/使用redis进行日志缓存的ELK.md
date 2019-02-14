
```
安装reids
# yum install -y redis

修改redis的配置文件
# vim /etc/redis.conf

修改内容如下
daemonize yes

bind 192.168.1.202

启动redis服务
# /etc/init.d/redis restart

测试redis的是否启用成功
# redis-cli -h 192.168.1.202

输入info如果有不报错即可
redis 192.168.1.202:6379> info

redis_version:2.4.10
....

编辑配置redis-out.conf配置文件，把标准输入的数据存储到redis中
# vim /etc/logstash/conf.d/redis-out.conf

添加如下内容

input {
            stdin {}
}

output {

        redis {
                host => "192.168.1.202"
                port => "6379"
                password => 'test'
                db => '1'
                data_type => "list"
                key => 'elk-test'
        }
}   

运行logstash指定redis-out.conf的配置文件
# /u
sr/share/logstash/bin/logstash -f /etc/logstash/conf.d/redis-out.conf


```




将数据输入到redis高速缓存中
```
所有的日志监控的来源文件都存放到redis中，然后通过redis在输出到elasticsearch中

更改为如下，编辑full.conf
input {
    file {
            path => "/var/log/httpd/access_log"
            type => "http"
            start_position => "beginning"
    }

    file {
            path => "/usr/local/nginx/logs/elk.access.log"
            type => "nginx"
            start_position => "beginning"
    }

    file {
            path => "/var/log/secure"
            type => "secure"
            start_position => "beginning"
    }

    file {
            path => "/var/log/messages"
            type => "system"
            start_position => "beginning"
    }
}


output {
    if [type] == "http" {
        redis {
            host => "192.168.1.202"
            password => 'test'
            port => "6379"
            db => "6"
            data_type => "list"
            key => 'nagios_http'
        }
    }

    if [type] == "nginx" {
        redis {
            host => "192.168.1.202"
            password => 'test'
            port => "6379"
            db => "6"
            data_type => "list"
            key => 'nagios_nginx'
        }
    }

    if [type] == "secure" {
        redis {
            host => "192.168.1.202"
            password => 'test'
            port => "6379"
            db => "6"
            data_type => "list"
            key => 'nagios_secure'
        }
    }

    if [type] == "system" {
        redis {
            host => "192.168.1.202"
            password => 'test'
            port => "6379"
            db => "6"
            data_type => "list"
            key => 'nagios_system'
        }
    }
}


运行logstash指定shipper.conf的配置文件
# /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/full.conf

在redis中查看是否已经将数据写到里面(有时候输入的日志文件不产生日志，会导致redis里面也没有写入日志)

```

将redis中的所有日志信息读取出来存入elasticsearch
```
把redis中的数据读取出来，写入到elasticsearch中(需要另外一台主机做实验)

编辑配置文件
# vim /etc/logstash/conf.d/redis-out.conf

添加如下内容
input {
    redis {
        type => "system"
        host => "192.168.1.202"
        password => 'test'
        port => "6379"
        db => "6"
        data_type => "list"
        key => 'nagios_system'
    batch_count => 1
     }

    redis {
        type => "http"
        host => "192.168.1.202"
        password => 'test'
        port => "6379"
        db => "6"
        data_type => "list"
        key => 'nagios_http'
    batch_count => 1
     }

    redis {
        type => "nginx"
        host => "192.168.1.202"
        password => 'test'
        port => "6379"
        db => "6"
        data_type => "list"
        key => 'nagios_nginx'
    batch_count => 1
     }

    redis {
        type => "secure"
        host => "192.168.1.202"
        password => 'test'
        port => "6379"
        db => "6"
        data_type => "list"
        key => 'nagios_secure'
    batch_count => 1
    }
}

output {

    if [type] == "system" {
        elasticsearch {
            hosts => ["192.168.1.202:9200"]
            index => "nagios-system-%{+YYYY.MM.dd}"
        }
    }   

    if [type] == "http" {
        elasticsearch {
            hosts => ["192.168.1.202:9200"]
            index => "nagios-http-%{+YYYY.MM.dd}"
        }   
    }   

    if [type] == "nginx" {
        elasticsearch {
            hosts => ["192.168.1.202:9200"]
            index => "nagios-nginx-%{+YYYY.MM.dd}"
        }   
    }  

    if [type] == "secure" {
        elasticsearch {
            hosts => ["192.168.1.202:9200"]
            index => "nagios-secure-%{+YYYY.MM.dd}"
        }   
    }  
}


注意:
input是从客户端收集的
output是同样也保存到192.168.1.202中的elasticsearch中，如果要保存到当前的主机上，可以把output中的hosts修改成localhost，如果还需要在kibana中显示，需要在本机上部署kabana，为何要这样做，起到一个松耦合的目的
说白了，就是在客户端收集日志，写到服务端的redis里或是本地的redis里面，输出的时候对接ES服务器即可

运行命令看看效果
# /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/redis-out.conf

```


定期删除日志
```
因为ES保存日志是永久保存，所以需要定期删除一下日志，下面命令为删除指定时间前的日志

curl -X DELETE http://xx.xx.com:9200/logstash-*-`date +%Y-%m-%d -d "-$n days"`
```
