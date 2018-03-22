#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 上午9:59
# @Author  : Jio Chen
# @Desc    : 练习 2-3

name = "Eric"
message = "Hello " + name + ", would you like to learn some Python today?"
print(message)

name = "jio chen"
message = "Hello " + name.lower() + ", would you like to learn some Python today?"
print(message)

message = "Hello " + name.upper() + ", would you like to learn some Python today?"
print(message)

message = "Hello " + name.title() + ", would you like to learn some Python today?"
print(message)

message = 'Albert Einstein once said, "A person who never made a mistake new tried anything new."'
print(message)

famous_person = "Albert Einstein"
message = famous_person + ' once said, "A person who never made a mistake new tried anything new."'
print(message)

name = "\t\njio chen"
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())
