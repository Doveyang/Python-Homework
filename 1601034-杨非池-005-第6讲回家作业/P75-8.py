# -*- coding:utf-8 -*-
####################################
# File name: P75-8.py              #
# Author: Nick Yang                #
# Date created: 4/2/2017           #
# Date last modified: 4/2/2017     #
# Python Version: 2.7              #
####################################

a = [87, 32, 53, 2, 3, 53, 8, 13, 68, 4]
a[::2] = sorted(a[::2])
print a

'''
a = [87, 32, 53, 2, 3, 53, 8, 13, 68, 4]
flag = True
length = 10
while flag:
    flag = False
    for i in range(2, length, 2):
        if a[i - 2] > a[i]:
            a[i-2], a[i] = a[i], a[i-2]
            flag = True
    length -= 2
print a
'''