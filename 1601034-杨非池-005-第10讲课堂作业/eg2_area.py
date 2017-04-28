# -*- coding: UTF-8 -*-
from math import *
def circle(r):
    area = pi * r * r
    perimeter = 2 * pi * r
    print u'半径为',r,u'的圆面积为：%.2f' % area
    print u'半径为',r,u'的圆周长为：%.2f' % perimeter

circle(2)
circle(3)
circle(4)
