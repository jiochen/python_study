#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午3:44
# @Author  : Jio Chen
# @Desc    : 练习 6-7

print("##################################################")

person_info_0 = {
    'first_name': '陈',
    'last_name': '浩',
    'age': 30,
    'city': '合肥'
}

person_info_1 = {
    'first_name': '刘',
    'last_name': '敏',
    'age': 31,
    'city': '合肥'
}

person_info_2 = {
    'first_name': '陈',
    'last_name': '子曰',
    'age': 1,
    'city': '合肥'
}

persons = [person_info_0, person_info_1, person_info_2]

for person_info in persons:
    print(person_info)
