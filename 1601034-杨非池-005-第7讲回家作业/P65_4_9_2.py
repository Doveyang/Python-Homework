# -*- coding:utf-8 -*-
####################################
# File name: P65_4_9_2.py          #
# Author: Nick Yang                #
# Date created: 4/7/2017           #
# Date last modified: 4/7/2017     #
# Python Version: 2.7              #
####################################

print u'所有水仙花数是'
a = filter(lambda i: int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3 == i, range(100, 1000))
for x in a:
    print x, '\t',
