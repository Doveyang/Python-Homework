# -*- coding:utf-8 -*-
####################################
# File name: P75-7.py              #
# Author: Nick Yang                #
# Date created: 4/2/2017           #
# Date last modified: 4/2/2017     #
# Python Version: 2.7              #
####################################

a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
a = filter(lambda x: x % 2 == 0, a)
print a

'''
a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
i = 0
b = []
while i <= 9:
    if a[i] % 2 == 0:
        b.append(a[i])
    i += 1

print b
'''
