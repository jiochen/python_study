#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 上午11:32
# @Author  : Jio Chen
# @Desc    : 练习 4-12

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite food are:")
for food in my_foods:
    print(food)

print("\n")

print("My friend favorite food are:")
for food in friend_foods:
    print(food)
