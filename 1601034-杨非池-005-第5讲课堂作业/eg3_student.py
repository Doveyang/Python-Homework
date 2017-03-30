# -*- coding:utf-8 -*-
def judge_age(age):
	if age > 25:
		return 1
	elif age < 28:
		return 2
	else:
		return 0

def judge_major(major):
	if major == 1: #电子信息工程
		return  1
	elif major ==2: #计算机专业
		return 2
	else:
		return 0

def judge_college(college):
	if college ==1: #重点大学
		return 1
	else:
		return 0
		
age = judge_age(24)
majior = judge_major(2)
college = judge_college(0)

if (age == 1 and majior == 1) or (college == 1 and majior == 1) or (age == 2 and majior ==2):
	print "恭喜，你已获得我公司面试机会"
else:
	print "抱歉，你未达到面试要求"
