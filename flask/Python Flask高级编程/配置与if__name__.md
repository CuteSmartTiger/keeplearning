#### 配置文件
同级目录下定义config文件：
方法一：
```
from config import DEBUG
```

方法二：
```
#导入同级别下的config模块
app.config.from_object['config']
#DEBUG要大写
debug = app.config['DEBUG']

```

#### if __name__ == '__main__'
```Python
if __name__ == '__main__':
    # nginx+uwsgi,如果没有if判断，则app.run会运行程序，
    # uwsgi服务也会启动程序
    app.run(host='0.0.0.0', debug=True, port='5000')
```
