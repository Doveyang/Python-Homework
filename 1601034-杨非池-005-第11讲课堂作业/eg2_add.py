# -*- coding: UTF-8 -*-
def accumlation(n):
    sumup = 0
    for i in range(1, n + 1):
        sumup += reduce(lambda x, y: x * y, range(1, i + 1))
    return sumup

i = 5
print '1!+2!+3!+4!+5!=%s' % accumlation(i)
