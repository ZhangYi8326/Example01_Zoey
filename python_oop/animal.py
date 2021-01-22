# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/22 22:51
@Auth ： Zoey
@File ：animal.py
@Description：
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.color = "read"
        self.age = 8
        self.gender = "女"

    # 定义类方法"animal_shout"
    def animal_shout(self):
        print(f"{self.name}饿了会叫")

    # 定义类方法"animal_run
    def animal_run(self):
        print(f"{self.name}吃饱了会跑")


if __name__ == '__main__':
    # 实例化Animal类
    animal = Animal("毛毛")
    # 调用"animal_shout"方法
    animal.animal_shout()
    # 调用"animal_run"方法
    animal.animal_run()
