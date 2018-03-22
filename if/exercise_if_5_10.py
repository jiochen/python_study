#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 下午3:01
# @Author  : Jio Chen
# @Desc    : 练习 5-10

current_users = ['admin', 'jio', 'jovanni', 'hao', 'rio']
new_users = ['admin', 'rio', 'liu', 'min', 'ziyue']

for user in new_users:
    if user.lower() in current_users:
        print("User " + user + " is already exist.")
    else:
        print("User " + user + " is available.")
