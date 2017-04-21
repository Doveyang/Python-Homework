# -*- coding:utf-8 -*-
####################################
# File name: P82_exam4.py          #
# Author: Nick Yang                #
# Date created: 4/21/2017          #
# Date last modified: 4/21/2017    #
# Python Version: 2.7              #
####################################
n = raw_input(u'请输入几个数字：')
numbers = n.split(',')
numbers = map(lambda x: float(x), numbers)
print sum(numbers)
