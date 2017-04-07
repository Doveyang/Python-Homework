# -*- coding: UTF-8 -*-
score = [50, 40, 20, 30, 10]
print u'原始数据：', score
mm = score[0]
a = len(score)

for j in range(0, a):
    if score[j] < mm:
        mm = score[j]
        b = j

print u'最小值为：', mm
print u'下标为：', b
