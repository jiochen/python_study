#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午1:52
# @Author  : Jio Chen
# 遍历字典中所有的键

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# 效果同 for name in favorite_languages() 一样，.keys()可以省略
for name in favorite_languages.keys():
    print(name.title())

print("--------------------")

friend_names = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friend_names:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

print("--------------------")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
