#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 下午2:56
# @Author  : Jio Chen
# @Desc    : 练习 5-8 5-9

users = ['admin', 'jio', 'jovanni', 'chen', 'rio']

# users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")
