#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午3:14
# @Author  : Jio Chen
# @Desc    : 练习 7-5

prompt = "\nPlease tell me how old are you: "

while True:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("The ticket costs $0.")
    elif age <= 12:
        print("The ticket costs $10.")
    else:
        print("The ticket costs $15.")
