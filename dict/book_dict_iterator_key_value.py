#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午1:12
# @Author  : Jio Chen
# 遍历字典中所有键值对

user_0 = {
    'username': '九井九山',
    'first_name': '陈',
    'last_name': '浩'
}

print(type(user_0.items()))

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("--------------------")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language is " + language.title())
