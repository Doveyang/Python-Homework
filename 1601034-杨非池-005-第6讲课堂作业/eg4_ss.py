# -*- coding: utf-8 -*-
n = input(u'请输入n的值：')
def sum(n):
    i = 1
    s = 0
    while i <= n:
        s += i
        i += 1
    return s

ss = 0
i = 1
while i <= n:
    ss += 1.0 / sum(i)
    i += 1

print ss
