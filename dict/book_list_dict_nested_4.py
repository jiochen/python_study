#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午3:30
# @Author  : Jio Chen
# 字典列表嵌套

print("##################################################")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + " favorite languages are:")
    for language in languages:
        print("\t" + language.title())

