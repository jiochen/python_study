#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午2:38
# @Author  : Jio Chen
# @Desc    : 在 while 循环中使用 break

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city != 'quit':
        print(city)
    else:
        break
