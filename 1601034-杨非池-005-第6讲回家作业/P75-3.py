# -*- coding:utf-8 -*-
####################################
# File name: P75-3.py              #
# Author: Nick Yang                #
# Date created: 4/2/2017           #
# Date last modified: 4/2/2017     #
# Python Version: 2.7              #
####################################
# 从0开始斐波那契数列

fib = lambda n: (1 + (-1) ** n) / 2 if n <= 2 else fib(n - 1) + fib(n - 2)

b = map(lambda x: fib(x), range(1, 21))

print b

'''
a = [0, 1]
i = 0
while i <= 19:
        if i >= 2:
            a.append(a[i - 2] + a[i - 1])
        i += 1

print a
'''