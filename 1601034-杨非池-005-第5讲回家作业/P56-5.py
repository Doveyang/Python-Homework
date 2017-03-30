# -*- coding:utf-8 -*-
####################################
# File name: P56-5.py              #
# Author: Nick Yang                #
# Date created: 2/7/2017           #
# Date last modified: 3/30/2017    #
# Python Version: 2.7              #
####################################

x = input(u"请输入自变量：\n>")
if x < -5:
    y = x + 9
elif x >= 5:
    y = x + x - 15
else:
    y = x * x + 2 * x + 1

print y
