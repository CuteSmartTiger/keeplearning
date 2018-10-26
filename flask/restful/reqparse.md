[参数解析](http://www.pythondoc.com/Flask-RESTful/quickstart.html)


- 基本格式
```
寻找在 flask.Request.values 字典里的两个参数。一个类型为 int，另一个的类型是 str

from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate cannot be converted')
parser.add_argument('name', type=str)
args = parser.parse_args()


```

- [reqparse模块](http://www.pythondoc.com/Flask-RESTful/api.html#module-reqparse)
- [inputs模块](http://www.pythondoc.com/Flask-RESTful/api.html#module-flask.ext.restful.inputs)




- has_key
```
Python 3.X 里不包含 has_key() 函数，被 __contains__(key) 替代:

dict3 = {'name':'z','Age':7,'class':'First'};
print("Value : ",dict3.__contains__('name'))
print("Value : ",dict3.__contains__('sex'))
```
