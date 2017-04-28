# -*- coding: UTF-8 -*-
def run(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

year = input(u'请输入一个年份：')
if run(year):
    print 'Y'
else:
    print 'N'
