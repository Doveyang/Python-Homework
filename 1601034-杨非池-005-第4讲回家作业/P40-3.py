# -*- coding:utf-8 -*-
####################################
# File name: P40-3.py              #
# Author: Nick Yang                #
# Date created: 2/6/2017           #
# Date last modified: 3/20/2017    #
# Python Version: 2.7              #
####################################

b = []
while True:
    c = input("请输入值...\n>")
    if c != 0:
        b.append(c)
    else:
        break
t = tuple(b)
print t
