#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午2:33
# @Author  : Jio Chen
# @Desc    : 在 while 循环中添加标志

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message != 'quit':
        print(message)
    else:
        active = False
