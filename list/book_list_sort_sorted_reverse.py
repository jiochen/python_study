#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 下午2:59
# @Author  : Jio Chen
# @Desc    : 列表排序和反转

# sort 方法是永久排序
cars = ['bmw', 'audi', 'subaru', 'toyota']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars)

# sorted 方法是临时排序
cars = ['bmw', 'audi', 'subaru', 'toyota']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))


# reverse 反转列表
cars = ['bmw', 'audi', 'subaru', 'toyota']
cars.reverse()

print(cars)

# 列表长度
cars = ['bmw', 'audi', 'subaru', 'toyota']
print(len(cars))
