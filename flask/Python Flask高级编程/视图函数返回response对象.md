#### 视图函数对返回内容进行处理

返回response对象
```python
@app.route('/hello/')
def hello():
    # response对象包含信息
    # status code,200,404,301
    # content-type http headers
    # content-type = text/html
    # 当返回状态码为301时，会重定向到location页面上
    headers = {
        'content-type':'application/json',
        'location':'http://www.baidu.com'
    }
    response = make_response('<html></html>',301)
    response.headers = headers
    return response
```

优化简写：
```python
@app.route('/hello/')
def hello():
    headers = {
        'content-type':'application/json',
        'location':'http://www.baidu.com'
    }
    return '<html></html>',301,headers
```
