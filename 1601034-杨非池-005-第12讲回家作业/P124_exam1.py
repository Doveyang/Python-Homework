# -*- coding:utf-8 -*-
####################################
# File name: P124_exam1.py         #
# Author: Nick Yang                #
# Date created: 5/15/2017          #
# Date last modified: 5/15/2017    #
# Python Version: 2.7              #
####################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f = open('P124_exam1.txt', 'w')
s = u'abc123@#$中国人民'
f.write(s)
f.close()

f = open('P124_exam1.txt', 'r')
print u'字符串长度为:%s' % len(f.read())
