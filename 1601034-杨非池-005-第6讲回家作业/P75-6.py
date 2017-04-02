# -*- coding:utf-8 -*-
####################################
# File name: P75-6.py              #
# Author: Nick Yang                #
# Date created: 4/2/2017           #
# Date last modified: 4/2/2017     #
# Python Version: 2.7              #
####################################

a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
a = map(lambda x: a[x], range(0, 9, 2))
print a

'''
a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
i = 0
b = []
while i <= 9:
    b.append(a[i])
    i += 2

print b
'''
