# -*- coding:utf-8 -*-
####################################
# File name: ex2.py                #
# Author: Nick Yang                #
# Date created: 5/9/2017           #
# Date last modified: 5/9/2017     #
# Python Version: 2.7              #
####################################


def ex2(*args):
    b = []
    avg = 1.0 * sum(args[0]) / len(args[0]) 
    b.append(avg)
    for i in range(0, len(args[0])):
        if args[0][i] > avg:
            b.append(args[0][i])
    return tuple(b)

t = (1, 2, 3, 4)
print ex2(t)
