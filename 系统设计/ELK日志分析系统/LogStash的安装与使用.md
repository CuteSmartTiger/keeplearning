- 安装

- 单行执行方式
执行logstash的命令
/opt/logstash/bin/logstash -e 'input { stdin { } } output { stdout {} }'


/opt/logstash/bin/logstash -e 'input { stdin { } } output { stdout {codec => rubydebug} }'


如果标准输出还有elasticsearch中都需要保留应该怎么玩，看下面
/opt/logstash/bin/logstas -e 'input { stdin { } } output { elasticsearch { hosts => ["192.168.1.202:9200"] } stdout { codec => rubydebug }}'

stdout 表示输出到屏幕可见


- logstash的配置文件
```
官方指南:
https://www.elastic.co/guide/en/logstash/current/configuration.html

创建配置文件01-logstash.conf
# vim /etc/logstash/conf.d/01-logstash.conf

文件中添加以下内容
input { stdin { } }
output {
  elasticsearch { hosts => ["192.168.1.202:9200"] }
  stdout { codec => rubydebug }
}

使用配置文件运行logstash
/opt/logstash/bin/logstash -f /etc/logstash/conf.d/01-logstash.conf
```

   - 搜索指定file
   ```
     file插件的使用
      # vim /etc/logstash/conf.d/elk.conf

      添加如下配置
      input {
          file {
              path => "/var/log/messages"
              type => "system"
              start_position => "beginning"
              }
      }
      output {    
               elasticsearch {
                      hosts => ["192.168.1.202:9200"]
                      index => "system-%{+YYYY.MM.dd}"
                  }
      }


    #运行logstash指定elk.conf配置文件，进行过滤匹配，末尾的&表示后台运行
    /opt/logstash/bin/logstash -f /etc/logstash/conf.d/elk.conf &    

   ```

   - 收集多个文件的日志
   ```
   # vim /etc/logstash/conf.d/elk.conf

    添加secure日志的路径
    input {
        file {
            path => "/var/log/messages"
            type => "system"
            start_position => "beginning"
        }

        file {
            path => "/var/log/secure"
            type => "secure"
            start_position => "beginning"
        }
    }

    output {

        if [type] == "system" {

            elasticsearch {
                hosts => ["192.168.1.202:9200"]
                index => "nagios-system-%{+YYYY.MM.dd}"
            }
        }

        if [type] == "secure" {

            elasticsearch {
                hosts => ["192.168.1.202:9200"]
                index => "nagios-secure-%{+YYYY.MM.dd}"
            }
        }
    }

    运行logstash指定elk.conf配置文件，进行过滤匹配
    /opt/logstash/bin/logstash -f /etc/logstash/conf.d/elk.conf &
   ```

   - 多行日志
   ```
   添加如下配置
   input {
       stdin {
           codec => mutilline{     //多行模式，碰到指定模式之前，日志为无效，遇到模式时才将模式之前的信息 收集日志
             pattern => "^\["     //匹配模式
             negate => true       //无效
             what => "previous"   //之前
            }
       }
   }
   output {    
          stdout{
                   codec => "rubydebug"

               }
   }

   ```


   - 模块总结（面试）
      - file stdin stdout syslog tcp udp rubydebug mutilline
