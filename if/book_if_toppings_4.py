#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 下午2:24
# @Author  : Jio Chen
# @Desc    : if else

requested_toppings = ['mushrooms']

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
