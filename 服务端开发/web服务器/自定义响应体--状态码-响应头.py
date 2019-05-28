#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 14:49
# @Author  : liuhu
# @File    : 自定义响应体--状态码-响应头.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# coding:utf-8

from flask import Flask, make_response

app = Flask(__name__)


@app.route("/index")
def index():
    # 1 使用元组，返回自定义的响应信息
    #            响应体    状态码  响应头
    # return "index page", 400, [("Name", "pyton"), ("City", "shenzhen")]  # 响应头可以是列表
    # return "index page", 400, {"Name": "python1", "City1": "sz1"}  # 响应头可以是字典
    # return "index page", "666 状态码说明信息", {"Name1": "python1", "City1": "sz1"}  # 可以是非标准状态码
    # return "index page", "666 状态码说明信息"   # 可以缺省响应头

    # 2 使用make_response 来构造响应信息
    resp = make_response("index page 2")  # 响应体
    resp.status = "666 状态码说明信息"  # 设置状态码 (可以是非标准的状态码)
    resp.headers["city"] = "sz"  # 设置响应头
    return resp


if __name__ == '__main__':
    app.run(debug=True)
