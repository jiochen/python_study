#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午4:16
# @Author  : Jio Chen
# @Desc    : 练习 6-10

print("##################################################")

favorite_numbers = {
    'hao': [1, 2, 3],
    'min': [5],
    'zuyue': [6, 7, 8, 9]
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))
