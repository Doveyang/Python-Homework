# -*- coding: UTF-8 -*-
for i in range(1, 10):
    for j in range(1, i + 1):
        # print str(i) + '*' + str(j) + '=' + str(i*j) + '\t',
        print '%d*%d=%-2d' % (i, j, i * j),
    print
