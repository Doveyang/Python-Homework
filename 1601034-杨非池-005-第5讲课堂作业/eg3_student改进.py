# -*- coding:utf-8 -*-
def judge_age(age):
	if age > 25:
		return 1
	elif age < 28:
		return 2
	else:
		return 0

def judge_major(major):
	if major == 1: #������Ϣ����
		return  1
	elif major ==2: #�����רҵ
		return 2
	else:
		return 0

def judge_college(college):
	if college ==1: #�ص��ѧ
		return 1
	else:
		return 0
		
age = judge_age(int(raw_input("���������䣺\n>")))
majior = judge_major(int(raw_input("��ѡ��רҵ��\n1.������Ϣ����רҵ\n2.�����רҵ\n>")))
college = judge_college(int(raw_input("�Ƿ����ص��ѧ��\n�ǣ�1��\n��0��\n>")))

if (age == 1 and majior == 1) or (college == 1 and majior == 1) or (age == 2 and majior ==2):
	print "��ϲ�����ѻ���ҹ�˾���Ի���"
else:
	print "��Ǹ����δ�ﵽ����Ҫ��"