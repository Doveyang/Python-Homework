# -*- coding:utf-8 -*-
####################################
# File name: P82_exam5.py          #
# Author: Nick Yang                #
# Date created: 4/21/2017          #
# Date last modified: 4/21/2017    #
# Python Version: 2.7              #
####################################
n = raw_input(u'请输入一个字符串：')
location = raw_input(u'请输入位置：')
locations = location.split(',')
char = n[int(locations[0]):int(locations[1])]
print u'长度为: %s, 子串为：%s' % (len(n), char)
