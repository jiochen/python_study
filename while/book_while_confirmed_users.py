#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午3:21
# @Author  : Jio Chen
# @Desc    : 使用 while 循环遍历列表

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have benn confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
