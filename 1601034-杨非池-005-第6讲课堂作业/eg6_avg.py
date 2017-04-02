# -*- coding: utf-8 -*-
s = 0.0
i = 1
while 1:
    score = input(u'请输入一个成绩：')
    s += score
    flag = raw_input(u'是否继续输入？')
    if flag == 'y':
        i += 1
        continue
    else:
        break

average = s / i
print average
