# -*- coding:utf-8 -*-
####################################
# File name: exam5.py              #
# Author: Nick Yang                #
# Date created: 4/7/2017           #
# Date last modified: 4/7/2017     #
# Python Version: 2.7              #
####################################

n = 0
for i in range(2, 101):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        n += 1
        print i, '\t',

print u'\n共%r个' % n