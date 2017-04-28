# -*- coding:utf-8 -*-
####################################
# File name: P94-4.py              #
# Author: Nick Yang                #
# Date created: 4/28/2017          #
# Date last modified: 4/28/2017    #
# Python Version: 2.7              #
####################################
from math import *


def Area((a, b, c)):
    if a + b > c and a + c > b and b + c > a:
        p = 1.0 * (a + b + c) / 2
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        return u'面积为:%.2f' % area
    else:
        return u'不能构成三角形'

print Area(input(u'请输入三个数字：'))

