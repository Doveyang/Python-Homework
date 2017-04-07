# -*- coding:utf-8 -*-
####################################
# File name: P65_4_8.py            #
# Author: Nick Yang                #
# Date created: 4/7/2017           #
# Date last modified: 4/7/2017     #
# Python Version: 2.7              #
####################################

print u'1~100之间能被7整除，但不能同时被五整除的所有数'

for i in range(0, 101):
    if i % 7 == 0 and i % 5 != 0:
        print i, '\t',

