# -*- coding: UTF-8 -*-
s = raw_input(u'请输入几个数字，用逗号分割：')
list = s.split(',')
list = [float(x) for x in list]
print list
print sum(list)
