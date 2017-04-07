# -*- coding: UTF-8 -*-
s = ''
for i in range(1, 5):
    for j in range(1, 2*i):
        s += '*'
    print s
    s = ''
