#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 上午11:07
# @Author  : Jio Chen
# @Desc    : 字典的定义取值修改和添加键值对

# 字典的定义
alien_0 = {'color': 'green', 'points': 5}

# 字典的取值
print(alien_0['color'])
print(alien_0['points'])

# 添加键值对到字典中
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print("--------------------")

print("The alien is " + alien_0['color'] + ".")

# 修改字典中的值
alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + ".")
