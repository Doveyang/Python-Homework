# -*- coding: utf-8 -*-
n, m = input(u"请输入站数，人数")
if 1 <= n <= 4:
    pay = 3 * m
elif 5 <= n <= 9:
    pay = 4 * m
elif n > 9:
    pay = 5 *m
else:
    pay = '错误'

print pay
