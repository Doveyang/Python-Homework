# -*- coding:utf-8 -*-
####################################
# File name: P124_exam3.py         #
# Author: Nick Yang                #
# Date created: 5/15/2017          #
# Date last modified: 5/15/2017    #
# Python Version: 2.7              #
####################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f = open('P124_exam3.txt', 'w')
s = u'>Hi AaBbHi CcDdoO0Ll1a2a3a4a@#$Hi a>A Hi peach!=banana'
f.write(s)
f.close()

f = open('P124_exam3.txt', 'r')
text = f.read()
f.close()

f = open('P124_exam3.txt', 'w')
f.write(text.lower())
f.close()
