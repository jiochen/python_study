#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 下午2:38
# @Author  : Jio Chen
# @Desc    : 练习 3-4 3-5 3-6 3-7

guests = ['Henry', 'Wilshere', 'Ramsey', 'Wenger']
print("Please join me for dinner, " + guests[0])
print("Please join me for dinner, " + guests[1])
print("Please join me for dinner, " + guests[2])
print("Please join me for dinner, " + guests[3])

lose_guest = guests[-1]
print(lose_guest + " can't join dinner.")

new_guest = 'Walcott'
guests[-1] = new_guest

print("Please join me for dinner, " + guests[0])
print("Please join me for dinner, " + guests[1])
print("Please join me for dinner, " + guests[2])
print("Please join me for dinner, " + guests[3])

print("I have found more big desk.")
guests.insert(0, 'Ozil')
guests.insert(2, 'Sanchez')
guests.append('Aubameyang')

print("Please join me for dinner, " + guests[0])
print("Please join me for dinner, " + guests[1])
print("Please join me for dinner, " + guests[2])
print("Please join me for dinner, " + guests[3])
print("Please join me for dinner, " + guests[4])
print("Please join me for dinner, " + guests[5])
print("Please join me for dinner, " + guests[6])

print("I just can inviting 2 person for dinner with me.")
no_guest_1 = guests.pop()
no_guest_2 = guests.pop()
no_guest_3 = guests.pop()
no_guest_4 = guests.pop()
no_guest_5 = guests.pop()

print("Sorry " + no_guest_1 + ", I can't invite dinner with you.")
print("Sorry " + no_guest_2 + ", I can't invite dinner with you.")
print("Sorry " + no_guest_3 + ", I can't invite dinner with you.")
print("Sorry " + no_guest_4 + ", I can't invite dinner with you.")
print("Sorry " + no_guest_5 + ", I can't invite dinner with you.")

print("Please join me for dinner also, " + guests[0])
print("Please join me for dinner also, " + guests[1])

del guests[0]
del guests[0]

print(guests)
