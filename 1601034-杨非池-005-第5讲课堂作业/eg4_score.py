# -*- coding: utf-8 -*-
score = input(u'请输入你的成绩（0-100）：')
if score < 0 or score > 100:
    print u'无效成绩'
elif score >= 90:
    print u'优秀'
elif score >= 80:
    print u'良好'
elif score >= 70:
    print u'中等'
elif score >= 60:
    print u'及格'
else:
    print u'补考'
