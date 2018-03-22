#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午3:52
# @Author  : Jio Chen
# @Desc    : 练习 6-8

print("##################################################")

mimi = {
    'type': 'cat',
    'owner': '刘敏'
}

chuer = {
    'type': 'dog',
    'owner': '陈浩'
}

gaga = {
    'type': 'duck',
    'owner': '陈子曰'
}

pets = [mimi, chuer, gaga]

for pet in pets:
    print("The " + pet['type'] + " is owned by " + pet['owner'].title())
