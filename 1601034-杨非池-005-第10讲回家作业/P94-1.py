# -*- coding:utf-8 -*-
####################################
# File name: P94-1.py              #
# Author: Nick Yang                #
# Date created: 4/28/2017          #
# Date last modified: 4/28/2017    #
# Python Version: 2.7              #
####################################


def PM(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag


numbers = filter(lambda n: PM(n), range(2, 101))
for number in numbers:
    print number,
