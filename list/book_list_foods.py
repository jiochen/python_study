#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 下午3:32
# @Author  : Jio Chen
# @Desc    : 列表切片

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("My friend favorite foods are: ")
print(friend_foods)
