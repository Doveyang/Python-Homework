# -*- coding:utf-8 -*-
####################################
# File name: P52_3_6_hello.py      #
# Author: Nick Yang                #
# Date created: 3/30/2017          #
# Date last modified: 3/30/2017    #
# Python Version: 2.7              #
####################################

ques = input(u'你的话是：')
if ques in (u'你好', u'您好', u'hello'):
    print(u'您好')
elif ques in (u'请吃', u'请喝'):
    print(u'谢谢您')
else:
    print(u'对不起，我暂时不能理解。')

