#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午2:40
# @Author  : Jio Chen
# @Desc    : 练习 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

rolled_persons = ['jio', 'jen']

for person in rolled_persons:
    if person in favorite_languages.keys():
        print(person.title() + ", Thank you take the roll.")
    else:
        print(person.title() + ", Please take the roll.")
