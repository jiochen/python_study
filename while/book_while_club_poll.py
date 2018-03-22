#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午3:29
# @Author  : Jio Chen
# @Desc    : 使用 while 循环来填充字典

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which football club is your best love? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no)")

    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " loves the football club " + response.title())
