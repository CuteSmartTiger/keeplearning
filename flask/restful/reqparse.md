#### 极力推荐
- [Flask-RESTful ](https://flask-restful.readthedocs.io/en/latest/)


- 基本格式
```
寻找在 flask.Request.values 字典里的两个参数。一个类型为 int，另一个的类型是 str

from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate cannot be converted')
parser.add_argument('name', type=str)
args = parser.parse_args()

注意：当参数类型是列表时，只能解析出第一个索引值，比如
{u'package_id': 5, u'vms': [75, 15, 2]}
解析后为：:MultiDict([(u'package_id', 5), (u'vms', 75), (u'vms', 15), (u'vms', 2)])

原因为reqparse.resource方法中的values.update(value)，iter_multi_items
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
