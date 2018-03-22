#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午2:20
# @Author  : Jio Chen
# @Desc    : 练习 7-3

number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is times of 10.")
else:
    print("\nThe number " + str(number) + " is not times of 10.")
