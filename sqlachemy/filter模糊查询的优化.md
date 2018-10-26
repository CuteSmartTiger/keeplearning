背景：模型中Person类，假设有name address sex job salary 等



针对不同的字段进行条件查询，原始的方法：
```
for key in args:
  value = args[key]
  if key =='name':
     query = Person.query.filter(Person.name.ilike('%{!s}%'.format(value)))
  elif key == 'address':
     query = Person.query.filter(Person.address.ilike('%{!s}%'.format(value)))
  elif key == 'sex':
     query = Person.query.filter(Person.sex.ilike('%{!s}%'.format(value)))
  elif key == 'job':
     query = Person.query.filter(Person.job.ilike('%{!s}%'.format(value)))
  elif key == 'salary':
     query = Person.query.filter(Person.salary==value)
  else:
     return '没有这个字段',status.HTTP_406_NOT_ACCEPTABLE
```

优化：
```
for key in args:
  value = args[key]
  if value is not None:
      if isinstance(value,str):
          query = Terminal.query.filter(getattr(Person,key).ilike('%{!s}%'.format(value)))
      elif isinstance(value,(int,unicode)):
          query = Terminal.query.filter(getattr(Person,key)==value)
      else:
          return '没有这个字段',status.HTTP_406_NOT_ACCEPTABLE
```


- 可以了解一下：
[ython的hasattr() getattr() setattr() 函数使用方法详解](https://www.cnblogs.com/cenyu/p/5713686.html)
