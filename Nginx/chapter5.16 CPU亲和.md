减少进程切换对CPU性能的损耗


cat /proc/cpuinfo |grep "cpu cores"|uniq


cat /proc/cpuinfo |grep "processor"|wc -l   

查看物理CPU id
cat /proc/cpuinfo |grep "physical id"|sort|uniq|wc -l   

在vi /ect/nginx.conf中配置：
其中worker配置数量建议与实际相同

查看 进程与与编号
ps -eo pid,args,psr | grep [n]ginx


```
worker_processes;
#自动配置，不用再按序号配置worker_cpu_affinity
worker_cpu_affinity auto;
```


### Nginx通用配置优化：
```

user www-data;
worker_processes 4;
pid /run/nginx.pid;
#自动配置，不用再按序号配置worker_cpu_affinity
worker_cpu_affinity auto;

#要求高的可以设置两三万，一般小网站设置一万左右，根据实际情况
worker_rlimit_nofile 35535;

events {
  use epoll;

  worker_connections 768;
  # multi_accept on;
}

http {
        charset utf-8;    
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;

        types_hash_max_size 2048;
        # server_tokens off;

        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;


       gzip on;
       #不支持IE版本以下的
       gzip_disable "msie[1-6]\.";

       # gzip_vary on;
       # gzip_proxied any;
       # gzip_comp_level 6;
       # gzip_buffers 16 8k;
       # gzip_http_version 1.1;
       # gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;

```
