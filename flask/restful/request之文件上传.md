#### 三个主要知识点
1. 一个 <form> 标签被标记有 enctype=multipart/form-data ，并且在里面包含一个 <input type=file> 标签。
2. 服务端应用通过请求对象上的 files 字典访问文件。
3. 使用文件的 save() 方法将文件永久地保存在文件系统上的某处




#### 上传文件的强化优化
- file包含的信息有哪些方面



- 对文件中文名称的处理



- 文件的安全
  对文件名进行处理



- 大型文件上传失败（目前测试200MB以内可传）
（1）背景知识：
上传文件的大小超出了 Nginx 允许的最大值，如果没有配置的话，默认是1M；

（2）Nginx与文件相关的
上传文件大小相关的有三个配置
client_body_buffer_size 配置请求体缓存区大小, 不配的话，
client_body_temp_path 设置临时文件存放路径。只有当上传的请求体超出缓存区大小时，才会写到临时文件中
client_max_body_size 设置上传文件的最大值



1. 出现413 Request Entity Too Large异常
查看Nginx配置文件：
cat /etc/nginx/conf.d/desktop.conf
```
server {
    listen 80;
    server_name localhost;
    charset     utf-8;
    location / {
        try_files $uri @vdidesktop;
    }
    location ^~ /admin{
        alias /opt/www/dist/;
        try_files $uri $uri/   @rewrites;
    }
    location @rewrites {
            rewrite ^/(admin)/(.+)$ /$1/index.html last;
    }
    location @vdidesktop {
      include uwsgi_params;
      #uwsgi_pass unix:/tmp/uwsgi.sock;
      uwsgi_pass localhost:11000;
      rewrite ^/$ /admin redirect;
    }
    #client_max_body_size 200M;
    client_max_body_size 300M;
}

```
依然出现问题，调整lient_max_body_size的位置：从server层调到http层：
将desktop.conf中server里的文件尺寸大小注释，然后再主配置文件中：
```
http {
  client_max_body_size 300M
}
```
然后出现超时异常："message": "The data value transmitted exceeds the capacity limit."

2. 超时异常处理
```
proxy_connect_timeout 300s;
proxy_send_timeout 300s;
proxy_read_timeout 300s;
```
虽然不报超时异常，但是提示文件尺寸过大


```
 client_body_buffer_size 2048k;
 client_body_temp_path

```

3. 出现500 Internal Server Error异常
df -k 查看容器内部磁盘空间，单位是kb


- 提高上传文件的速度
队列+异步
服务端接收到数据后，直接存放到队列里，然后直接返回结果，然后服务端的应用再去队列里取数据 ，如果有问题的话，再向请求方推送一条数据，这样可以大大的提升效率，减少数据的数据库操作的等待




#### 参考文章
1. [上传文件](http://docs.jinkan.org/docs/flask/patterns/fileuploads.html#uploading-files)
2. [解决 413 Request Entity Too Large](https://blog.csdn.net/yinlongfei_love/article/details/81085761)
3. [提高Nginx网络吞吐量之buffers优化](https://www.cnblogs.com/felixzh/p/6283822.html)
4. [官网Nginx模块设置](http://nginx.org/en/docs/http/ngx_http_core_module.html#client_body_buffer_size)
