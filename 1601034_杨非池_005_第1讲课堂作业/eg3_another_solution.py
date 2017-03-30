# -*- coding:utf-8 -*-

x = raw_input('Please input a number.\n>')
a = x[0:1]
b = x[1:2]
c = x[2:3]

print '''
这个数的百位数是%s.
这个数的十位数是%s.
这个数的个位数是%s.
''' %(a, b, c)
