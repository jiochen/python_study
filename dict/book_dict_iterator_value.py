#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午2:15
# @Author  : Jio Chen
# 遍历字典中所有的值

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("The following languages have been montioned:")

for language in favorite_languages.values():
    print(language.title())

print("--------------------")

# 集合(set)类似于列表，每个元素独一无二
for language in set(favorite_languages.values()):
    print(language.title())
