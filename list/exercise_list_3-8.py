#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 下午3:36
# @Author  : Jio Chen
# @Desc    : 练习 3-8 3-9

places = ['chengdu', 'hangzhou', 'suzhou', 'kunming', 'haerbing']
print("original list: ")
print(places)

print("\n")

print("sorted list: ")
print(sorted(places))

print("\n")

print("original list: ")
print(places)

print("\n")

print("sorted reverse list: ")
print(sorted(places, reverse=True))

print("\n")

print("original list: ")
print(places)

print("\n")

places.reverse()
print("reverse list: ")
print(places)

print("\n")

places.reverse()
print("reverse again list: ")
print(places)

print("\n")
places.sort()
print("sort list: ")
print(places)

print("\n")

places.sort(reverse=True)
print("sort again list: ")
print(places)
