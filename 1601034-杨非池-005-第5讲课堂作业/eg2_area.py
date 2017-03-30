# -*- coding: utf-8 -*-
import math
r = input('请输入半径')
if r >= 0:
    s = math.pi * r ** 2
    print 's = pi * r * r =', s
else:
    print '半径输入有误'
