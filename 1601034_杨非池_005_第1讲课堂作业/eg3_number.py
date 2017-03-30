# -*- coding:utf-8 -*-

x = input('Please input a number.\n>')
a = x // 100
b = x % 100 // 10
c = x % 10

print '''
这个数的百位数是%d.
这个数的十位数是%d.
这个数的个位数是%d.
''' %(a, b, c)
