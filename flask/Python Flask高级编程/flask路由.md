#### 路由的注册方法：
1. 方法一
```
@app.route('/hello/')
def hello():
    return 'hello'
app.run(debug=True)

```
route是对add_url_rule方法的封装，可看源码


2. 方法二
```
def hello():
    return 'hello'

#view_func指定调用的函数
app.add_url_rule('/hello', view_func=hello)
app.run(debug=True)

```
flask中的路由函数可以理解为MVC中的c


#### 唯一URL与重定向

重定向的概念

尾部不加'/'需要重定向
