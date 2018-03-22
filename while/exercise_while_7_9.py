#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午3:44
# @Author  : Jio Chen
# @Desc    : 练习 7-9

sandwich_orders = ["reuben", "pastrami", "submarine", "pastrami", "pastrami"]

print("Sorry, Pastrami is sold out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
