# -*- coding:utf-8 -*-
####################################
# File name: P56-7.py              #
# Author: Nick Yang                #
# Date created: 2/7/2017           #
# Date last modified: 3/30/2017    #
# Python Version: 2.7              #
####################################

year = input(u'输入年份\n>')
if year % 400 == 0 or year % 4 == 0:
    print u"闰年"
else:
    print u"不是闰年"
