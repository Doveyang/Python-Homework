# -*- coding: cp936 -*-

studscore = {"��ɮ": 55, "�����": 78, "��˽�": 40, "ɳɮ": 96, "����": 65, "����": 92, "�׹Ǿ�": 70, "�캢��": 99, "̫���Ͼ�": 68, "������": 87}
studscore['̫�׽���'] = "ȱ��"
studscore['��ʴ��'] = 90
studscore['��ɮ'] = 60
del studscore['�׹Ǿ�']
print '������Ϊ��%r' % len(studscore)
name = raw_input('������������')
score = studscore[name]
print '�ɼ�Ϊ%r' % (score)
