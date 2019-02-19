- CBA
本质： 通过view将路由与类绑定，通过dispatch获取请求方法调用对应函数
流程：路由 view函数  dispatch(反射)
取消csrf认证，装饰器需要加到dispatch方法上

扩展：CSRF
    基于中间件的process_view方法
    装饰器给单独函数进行设置（认证或无需认证）

- 基于CBA的[restful规范](https://www.cnblogs.com/wupeiqi/articles/7805382.html)
 介绍 10个规范  剧本讲故事 演变
 跨域如何解决
