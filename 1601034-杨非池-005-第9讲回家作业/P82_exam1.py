# -*- coding:utf-8 -*-
####################################
# File name: P82_exam1.py          #
# Author: Nick Yang                #
# Date created: 4/21/2017          #
# Date last modified: 4/21/2017    #
# Python Version: 2.7              #
####################################
sentence = raw_input(u'请输入一个语句：')
if 'for' in sentence or 'while' in sentence:
    print u'是循环'
else:
    print u'不是循环'
