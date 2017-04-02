# -*- coding: utf-8 -*-
print u'请输入若干个数进行求和操作，当输入负数时结束：'
s = 0
x = input(u'请输入一个整数:')
while x >= 0:
    s += x
    x = input(u'请输入一个整数:')

print u'整数之和=', s
