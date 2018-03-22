#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 上午10:27
# @Author  : Jio Chen
# @Desc    : 列表元素的添加

# 当定义空列表时，如果不对其操作，直接添加添加元素会有警告
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)
