# -*- coding: utf-8 -*-
a = input(u'请输入第一个数：')
b = input(u'请输入第二个数：')
if a > b:
    (a, b) = (b, a)
print u'从小到大输出：', a, b
