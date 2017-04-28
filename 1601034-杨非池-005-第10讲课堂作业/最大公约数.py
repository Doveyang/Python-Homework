# -*- coding: UTF-8 -*-
def GCD((x, y)):
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y   
    return y

a = input(u'请输入两个整数：')
print u'最大公约数为：%s' % GCD(a)
