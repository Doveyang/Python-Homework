# -*- coding:utf-8 -*-
####################################
# File name: ex1.py                #
# Author: Nick Yang                #
# Date created: 5/9/2017           #
# Date last modified: 5/9/2017     #
# Python Version: 2.7              #
####################################
# 从0开始斐波那契数列
fib = lambda n: (1 + (-1) ** n) / 2 if n <= 2 else fib(n - 1) + fib(n - 2)
for i in range(0, 20):
    print u'第%s项：%s' % (i + 1, fib(i + 1))
