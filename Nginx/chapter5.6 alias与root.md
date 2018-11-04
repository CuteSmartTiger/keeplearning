- root
```
location /request_path/image/{
  root /local_path/image/;
}

http://www.baidu.com/request_path/image/cat.png

实际查找位置：
/local_path/image/request_path/image/cat.png

```


- alias
```
location /request_path/image/{
  alias /local_path/image/;
}

http://www.baidu.com/request_path/image/cat.png

实际查找位置：
/local_path/image/cat.png
```
