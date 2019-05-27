#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 14:28
# @Author  : liuhu
# @File    : app.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


from flask import Flask
import flask_restful

app = Flask(__name__)
api = flask_restful.Api(app)

import random


class HelloWorld(flask_restful.Resource):
    def get(self):
        num = random.randint(0, 100)
        print(num)
        return {'hello': 'world {}'.format(num)}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
