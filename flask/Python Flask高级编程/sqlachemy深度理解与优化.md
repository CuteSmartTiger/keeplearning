#### 初始化
方法一：
```python
db =SQAlchemy()
db.init_app(app)
db.create_all(app=app)
```

方法二：
```Python
db =SQAlchemy()
db.init_app(app)
with app.app_context():
    db.create_all()
```

方法三：
```Python
db =SQAlchemy(app)
db.init_app()
db.create_all()
```



#### 链式调用
```python
#query为链式调用的主体，query中的信息指定了返回的结果信息
#后面的为子函数，查询结果返回query
#遇到first()，all()进入查询
STUDENT.query.filter_by().group_by().order_by().limit().distinct().all()
```


#### db.session.query与MODEL.query 的区别

将需要两次查询才可以获得结果的方法，优化编写为一次查询，实例
```python
count_list = db.session.query(func.count(Wish.id),Wish.isbn).filter(Wish.launched == False,Wish.isbn.in_(isbn_list)),Wish.status==1).group_by(Wish.isbn).all()
count_list = [{'count':w[0],'isbn':w[1]}for w in count_list]
```


#### filter_by的重写优化
针对有假删除的业务
```python
class Query(BaseQuery):
  def filter_by(self,**kwargs):
    if 'status' not in kwargs.keys():
      kwargs['status'] = 1
    return super(Query,self).filter_by(**kwargs)

db = SQAlchemy(query_class=Query)

```
