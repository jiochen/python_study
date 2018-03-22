#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午2:29
# @Author  : Jio Chen
# @Desc    : 练习 6-5

rivers = {
    'chang jiang river': 'china',
    'nile': 'egypt',
    'mississippi river': 'american',
    'yellow river': 'china'
}

for river_name, country_name in rivers.items():
    print("The " + river_name.title() + " runs through " +
          country_name.title())

print("--------------------")

for river_name in rivers.keys():
    print(river_name.title())

print("--------------------")

for country_name in rivers.values():
    print(country_name.title())
