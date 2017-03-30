# -*- coding:utf-8 -*-
####################################
# File name: 01-01.py              #
# Author: Nick Yang                #
# Date created: 2/20/2017          #
# Date last modified: 2/28/2017    #
# Python Version: 2.7              #
####################################

def print_date(number):
    length = len(number)
    if length == 8:
        year = number[0:4]
        month = number[4:6]
        day = number[6:8]
        print("%s年%s月%s日") % (year, month, day)
    else:
        print "请输入八位数字！"


print_date(raw_input("请输入八位数字\n>"))
