#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 下午1:04
# @Author  : Jio Chen
# @Desc    : if else

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
