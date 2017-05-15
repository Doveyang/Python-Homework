# -*- coding: utf-8 -*-
f = open('Ques7_1.txt', 'r')
while 1:
    line = f.readline()
    if line == '':
        break
    print line,
f.close()
