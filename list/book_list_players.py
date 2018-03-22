#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 下午3:06
# @Author  : Jio Chen
# @Desc    : 列表切片

players = ['charles', 'martina', 'michael', 'florence', 'ali']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

print("--------------------")

print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())
