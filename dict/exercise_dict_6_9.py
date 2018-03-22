#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午4:09
# @Author  : Jio Chen
# @Desc    : 练习 6-9

print("##################################################")

favorite_places = {
    'jio': ['成都', '杭州', '苏州'],
    'min': ['三亚'],
    'ziyue': ['三亚', '北京']
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place)
