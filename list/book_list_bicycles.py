#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 上午9:52
# @Author  : Jio Chen
# @Desc    : 列表的定义和基本操作

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
