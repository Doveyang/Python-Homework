# -*- coding: UTF-8 -*-
score = []
for i in range(1, 6):
    x = input(u'请输入第' + str(i) + u'个元素：')
    score = score + [x]

print u'输入的数据为：', score
s = 0.0
for x in score:
    s += x
    
avg = s / len(score)
print u'平均分是：', avg
