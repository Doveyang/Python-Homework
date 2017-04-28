# -*- coding:utf-8 -*-
####################################
# File name: P94-2.py              #
# Author: Nick Yang                #
# Date created: 4/28/2017          #
# Date last modified: 4/28/2017    #
# Python Version: 2.7              #
####################################


def triangle((a, b, c)):
    if a + b > c and a + c > b and b + c > a:
        return True


flag = triangle(input(u'请输入三边长：'))
if flag:
    print u'能构成三角形'
else:
    print u'不能构成三角形'
