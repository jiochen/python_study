#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午3:37
# @Author  : Jio Chen
# @Desc    : 练习 7-8

sandwich_orders = ["reuben sandwich", "submarine sandwich"]
finished_sandwiches = []

while sandwich_orders:
    sandwich_name = sandwich_orders.pop()
    print("I made your " + sandwich_name.title())
    finished_sandwiches.append(sandwich_name)

print("\nAll of orders is finished: ")
while finished_sandwiches:
    print(finished_sandwiches.pop().title())
