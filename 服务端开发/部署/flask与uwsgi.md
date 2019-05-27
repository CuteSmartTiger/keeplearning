docker run -it docker.io/alpine:3.8 /bin/sh

echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.8/main/" > /etc/apk/repositories

apk add --no-cache vim nginx python3 uwsgi uwsgi-python3

ln -s /usr/bin/python3 /usr/bin/python
ln -s /usr/bin/pip3 /usr/bin/pip
python -m pip install --upgrade pip

pip install flask


- 在根目录下创建一个app目录
mkdir /app
 cd /app/
 vi app.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!!\n'


if __name__ == '__main__':
    app.run()

```



- 在app目录下创建并编辑uwsgi.ini文件(与应用文件app.py相同目录下)
```

[uwsgi]
uwsgi-socket    = 127.0.0.1:9000
callable        = app
plugin          = python3
wsgi-file       = app.py
buffer-size     = 65535
```

启动uwsgi
nohup uwsgi --ini uwsgi.ini &







- 配置Nginx
vi /etc/nginx/nginx.conf




docker run -p 9999:6666 -d web_app --name="liuhu"


#### 参考文章
- [Docker构建nginx+uwsgi+flask镜像](https://www.cnblogs.com/beiluowuzheng/p/10219506.html)
