#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 下午1:15
# @Author  : Jio Chen
# @Desc    : if if

banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'

if user in banned_users:
    print(user.title() + ", you can't post a response")

if user not in banned_users:
    print(user.title() + ", you can post a response")
