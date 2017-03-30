# -*- coding:utf-8 -*-
####################################
# File name: P40-4.py              #
# Author: Nick Yang                #
# Date created: 2/6/2017           #
# Date last modified: 3/20/2017    #
# Python Version: 2.7              #
####################################
d = {}

while True:
    a = raw_input("项目：\n>")
    if a != "0":
        b = raw_input("解释：\n>")
        d[a] = b
    else:
        break

e = d.keys()
f = d.values()

print e, f
