#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午2:22
# @Author  : Jio Chen
# @Desc    : 练习 6-4

dictionary = {
    'print': '打印',
    'list': '列表',
    'tuple': '元组',
    'dict': '字典',
    'string': '字符串',
    'int': '整型'
}

for key, value in dictionary.items():
    print(key + ": " + value)
