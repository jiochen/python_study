#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午3:10
# @Author  : Jio Chen
# 字典列表嵌套

print("##################################################")

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_count in range(30):
    alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(alien)

# 修改外星人的属性
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    else:
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# 显示前5个外星
for alien in aliens[:5]:
    print(alien)

print("...")

print("Tatal number of aliens: " + str(len(aliens)))
