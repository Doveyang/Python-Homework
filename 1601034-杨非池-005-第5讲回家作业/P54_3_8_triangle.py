# -*- coding:utf-8 -*-
####################################
# File name: P54_3_8_triangle.py   #
# Author: Nick Yang                #
# Date created: 3/30/2017          #
# Date last modified: 3/30/2017    #
# Python Version: 2.7              #
####################################

from math import *
a, b, c = input(u'请输入三边长：')
if a + b > c and a + c > b and b + c > a:
    p = 1.0 * (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    if a == b != c or a == c != b or b == c != a:
        result = u'等腰三角形'
    elif a == b == c:
        result = u'等边三角形'
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        result = u'直角三角形'
    else:
        result = u'普通三角形'
else:
    result = u'非三角形'

if result != u'非三角形':
    print u'三角形的面积是：%s' % str(area)
    print result
else:
    print u'三边构成：%s' % result
