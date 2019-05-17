#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 13:31
# @Author  : liuhu
# @File    : 自己编写web服务器.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def app(environ, start_response):
    data = b"hello"
    start_response("200 liuhu ", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

# gunicorn -w 4 myapp:app
