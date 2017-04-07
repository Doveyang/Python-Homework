# -*- coding:utf-8 -*-
####################################
# File name: exam9_6.py            #
# Author: Nick Yang                #
# Date created: 4/7/2017           #
# Date last modified: 4/7/2017     #
# Python Version: 2.7              #
####################################

for i in range(1, 8):
    print ' ' * abs(i - 4) + '*' * (7 - abs(2 * i - 8))
