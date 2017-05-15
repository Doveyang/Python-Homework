# -*- coding: utf-8 -*-
f = open('Ques7_1.txt', 'r')
i = 0
while 1:
    line = f.readline()
    if line == '':
        break
    print line,
    i = i + 1
f.close()
print i
