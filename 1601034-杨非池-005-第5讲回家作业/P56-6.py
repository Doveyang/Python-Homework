# -*- coding:utf-8 -*-
####################################
# File name: P56-6.py              #
# Author: Nick Yang                #
# Date created: 2/7/2017           #
# Date last modified: 3/30/2017    #
# Python Version: 2.7              #
####################################

list = ['张三', '李四', '王五', '赵六', '孙七']
name = raw_input(u"请输入名字:\n>")
if name in list:
    print u"找到此人"
else:
    print u"查无此人"
