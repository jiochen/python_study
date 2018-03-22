#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 下午4:11
# @Author  : Jio Chen
# @Desc    : 列表遍历

magicians = ['alice', 'david', 'caroline']

print("--------------------------------------------")

for magician in magicians:
    print(magician)

print("--------------------------------------------")

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("--------------------------------------------")

print("Thank you, everyone. That was a great magic show!")
