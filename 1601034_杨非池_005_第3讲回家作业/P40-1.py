# -*- coding:utf-8 -*-
####################################
# File name: P40-1.py              #
# Author: Nick Yang                #
# Date created: 2/4/2017           #
# Date last modified: 3/15/2017    #
# Python Version: 2.7              #
####################################

a = 1
b = []
while a != 0:
	a = input(u"请输入值，以0结束\n>")
	b.append(a)

print u"列表里的元素有："
print "-" * 20
i = 0
while i < len(b) - 1:
    print b[i]
    i += 1
