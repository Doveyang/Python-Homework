# -*- coding:utf-8 -*-
####################################
# File name: exam1_4.py            #
# Author: Nick Yang                #
# Date created: 4/7/2017           #
# Date last modified: 4/7/2017     #
# Python Version: 2.7              #
####################################

n = 1
while True:
    if 1.0 / (2 * n - 1) <= 1e-6:
        break
    else:
        n = n + 1

a = reduce(lambda x, y: x + (-1.0) ** (y - 1) * 1 / (2 * y - 1), range(1, n))

print u'计算了 %r 项，pi = %r' % (n, 4 * a)

'''
i = 1
s = 0
t = 1.0
while t > 1e-6:
    s += (-1) ** (i - 1) * t
    i += 1
    t = 1.0 / (2 * i - 1)

print u'计算了 %r 项，pi = %r' % (i, 4 * s)
'''
