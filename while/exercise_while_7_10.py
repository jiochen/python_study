#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午3:47
# @Author  : Jio Chen
# @Desc    : 练习 7-10

favorite_places = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    place_name = input("Where do you want to visit? ")

    favorite_places[name] = place_name

    repeat = input("Next one? (y / n)")
    if repeat == 'n':
        polling_active = False

print("\n----  Poll Results  ----")
for name, place_name in favorite_places.items():
    print(name.title() + " loves " + place_name.title())
