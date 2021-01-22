# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/22 22:52
@Auth ： Zoey
@File ：cat.py
@Description：
"""

from python_oop.animal import Animal


class Cat(Animal):
    def __init__(self):
        self.hair = "短毛"
        super().__init__("毛毛")

    # 子类中定义"catch_mouse"方法
    def catch_mouse(self):
        print(f"{self.name}会抓老鼠")
        super().animal_shout()

    # 重写父类"animal_shout"方法
    def animal_shout(self):
        print(f"{self.name}饿了会喵喵叫")


if __name__ == '__main__':
    # 实例化类
    cat = Cat()
    # 调用"catch_mouse"方法
    # cat.catch_mouse()
    # 调用重写的"animal_shout"方法
    cat.animal_shout()
