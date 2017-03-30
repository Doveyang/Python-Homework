# -*- coding: cp936 -*-

studscore = {"唐僧": 55, "孙悟空": 78, "猪八戒": 40, "沙僧": 96, "如来": 65, "观音": 92, "白骨精": 70, "红孩儿": 99, "太上老君": 68, "白龙马": 87}
studscore['太白金星'] = "缺考"
studscore['玉皇大帝'] = 90
studscore['唐僧'] = 60
del studscore['白骨精']
print '总人数为：%r' % len(studscore)
name = raw_input('请输入姓名：')
score = studscore[name]
print '成绩为%r' % (score)
