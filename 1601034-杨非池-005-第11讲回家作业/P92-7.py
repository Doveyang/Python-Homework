# -*- coding:utf-8 -*-
####################################
# File name: P92-7.py              #
# Author: Nick Yang                #
# Date created: 5/9/2017           #
# Date last modified: 5/9/2017     #
# Python Version: 2.7              #
####################################


def P95_7(char):
    up = []
    low = []
    number = []
    for x in char:
        if x.isupper():
            up.append(x)
        elif x.islower():
            low.append(x)
        elif x.isdigit():
            number.append(x)
    return [len(up), len(low), len(number)]


print P95_7(raw_input(u'请输入字符串：'))
