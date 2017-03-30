# -*- coding:utf-8 -*-
####################################
# File name: P23-2.py              #
# Author: Nick Yang                #
# Date created: 2/4/2017           #
# Date last modified: 3/4/2017     #
# Python Version: 2.7              #
####################################

import math


def input_dot(dot):
    element = []
    part = dot.split(',')
    part1 = part[0].strip()
    part2 = part[1].strip()
    x = int(part1.strip('('))
    y = int(part2.strip(')'))
    element.append(x)
    element.append(y)
    return element


number1 = input_dot(raw_input("请输入一个第一象限的坐标，例：(3,4)\n>"))
number2 = input_dot(raw_input("请输入一个第三象限的坐标，例：(-3,-4)\n>"))

a, b, c, d = number1[0], number1[1], number2[0], number2[1]

distance = math.sqrt((a - c) * (a - c) + (b - d) * (b - d))

print '两点间的距离是%r' % distance
