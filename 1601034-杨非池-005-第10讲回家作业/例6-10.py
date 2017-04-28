# -*- coding:utf-8 -*-
####################################
# File name: 例6-10.py             #
# Author: Nick Yang                #
# Date created: 4/28/2017          #
# Date last modified: 4/28/2017    #
# Python Version: 2.7              #
####################################
def rectangle(x, y):
    area = x * y
    perimeter = 2 * (x + y)
    print u'矩形面积为：', area
    print u'矩形周长为：', perimeter


a = input(u'请输入矩形的长：')
b = input(u'请输入矩形的宽：')
rectangle(a, b)
