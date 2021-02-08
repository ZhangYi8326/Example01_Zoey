# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/8 13:59
@Auth ： Zoey
@File ：money.py
@Description：
"""


class CountSalary:
    def __init__(self):
        # 已有工资
        self.saved_money = 1000
        # 每月工资
        self.month_salary = 1000

    def send_money(self):
        print("发工资啦")
        # 计算发工资后的剩余金额
        self.saved_money += self.month_salary
        # 返回发工资后的金额
        return self.saved_money


if __name__ == '__main__':
    countsalary = CountSalary()
    print(countsalary.send_money())
