#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 下午2:40
# @Author  : Jio Chen
# @Desc    : 练习 4-3 4-4 4-5 4-6

for value in range(1, 21):
    print(value)

print("--------------------------")

numbers = list(range(1, 1000001))
for value in numbers:
    print(value)

print("--------------------------")

print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("--------------------------")

numbers = list(range(1, 21, 2))

for value in numbers:
    print(value)

print("--------------------------")
