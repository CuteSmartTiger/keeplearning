#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 15:09
# @Author  : liuhu
# @Site    : 
# @File    : 结构型之适配器模式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'


class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        # print(adapted_methods)
        # print(self.__dict__)
        print(self.__dict__.update(adapted_methods))
        # print(self.__dict__)

    def __getattr__(self, item):
        return getattr(self.obj, item)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))

    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))
    for i in objects:
        print('{} {}'.format(str(i), i.execute()))
        print(i.name)


if __name__ == "__main__":
    main()
