#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午3:10
# @Author  : Jio Chen
# @Desc    : 练习 7-4

prompt = "\nPlease enter a pizza topping:"
prompt += "\n(Enter 'quit' to end to program). "

active = True

while active:
    topping = input(prompt)

    if topping != 'quit':
        print(topping)
    else:
        active = False
