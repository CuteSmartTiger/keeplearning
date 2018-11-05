### Nginx架构的安全篇

1.常见恶意行为（爬虫 恶意抓取 资源盗用）-------不违法
针对行为进行分析
基础防盗链 防止爬虫

secure_link_module 针对核心重要数据

access_module 对后台的文件或者用户的部分服务数据



2.常见的攻击手段  ----- 违法
- 后台密码撞库，密码复杂，采用新算法
access_module 对后台提供IP防控
预警机制



- 文件上传漏洞
后台代码对文件的类型与内容进行判断
同时可以在Nginx中：针对上传的图片进行后缀的判断
```
location ^~ /upload {
  root/opt/app/images;
  if($request_filename ~*(.*)\.php){
    return 403
  }
}
```

- SQL注入
用户名：'or 1=1#
密码：321
解决方法：
方法一：开发时进行判断

方法二：Nginx加lua防火墙
[配置初始文件](https://github.com.loveshell/ngx_lua_waf)
