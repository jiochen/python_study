#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 上午11:25
# @Author  : Jio Chen
# @Desc    : 练习 4-11

my_pizzas = ["Seafoot pizza", "Pepperoni pizza", "Chicken pizza"]
friend_pizzas = my_pizzas[:]

my_pizzas.append('Hawaii pizza')
friend_pizzas.append('Salmon pizza')

print("My favorite pizza are:")
for pizza in my_pizzas:
    print(pizza)

print("\n")

print("My friend favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza)
