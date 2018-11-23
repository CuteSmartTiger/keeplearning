#### 思考的问题清单
- 从普通http请求定义的路由函数如何演变为注册蓝图的路由函数，以及restfulAPI的思路的强化



####  注册蓝图
规范：务必保证蓝图的名称与__init__.py中注册的uri一致

生成蓝图应用模块
group_page_v2 = Blueprint('v2/groups', __name__)
绑定API
group_api_v2 = Api(group_page_v2)   
在groups模块下添加API资源
group_api_v2.add_resource(GroupListAPI, '/', endpoint='api')
group_api_v2.add_resource(GroupAPI, '/<int:id>', endpoint='api_id')


在__init__.py进行蓝图注册：
app.register_blueprint(group_page_v2, url_prefix='/v2/groups')

url_prefix是指定[挂载点](http://flask.pocoo.org/docs/0.12/blueprints/)，即指定应用模块，所以此处必须与蓝图模块中保持一致
