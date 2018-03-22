#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 上午11:08
# @Author  : Jio Chen
# @Desc    : 列表弹出和删除元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

# 默认弹出最后一个元素
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned)

# 弹出指定位置的元素
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned)

# 根据值删除元素
# 方法remove()只删除第一个指定的值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
