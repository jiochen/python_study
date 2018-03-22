#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午3:23
# @Author  : Jio Chen
# 字典列表嵌套

print("##################################################")

# 存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# 概述所点的披萨
print("you ordered a " + pizza['crust'] + '-crust pizza ' +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
