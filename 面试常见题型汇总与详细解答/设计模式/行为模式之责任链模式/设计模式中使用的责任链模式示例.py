#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 15:06
# @Author  : liuhu
# @Site    : 
# @File    : 设计模式中使用的责任链模式示例.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        print('初始化父类为 {0}'.format(parent))
        self.parent = parent

    def handle(self, event):
        handler = 'handle_{}'.format(event)
        print('当前Handel is {0}'.format(handler))
        if hasattr(self, handler):
            print('当前实例拥有{0}方法'.format(handler))
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            print('调用父类的{0}方法'.format(handler))
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            print('调用handle_default方法')
            self.handle_default(event)


class MainWindow(Widget):

    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):

    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):

    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()

    sd = SendDialog(mw)
    msg = MsgText(sd)
    cout = 0
    print('for in ')
    for e in ('down', 'paint', 'unhandled', 'close'):
        if cout ==1 :
            break
        evt = Event(e)
        # print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        # print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        # print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)
        # print('\n  ====================')
        cout +=1


if __name__ == '__main__':
    main()
