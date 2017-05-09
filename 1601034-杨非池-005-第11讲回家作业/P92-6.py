# -*- coding:utf-8 -*-
####################################
# File name: P92-6.py              #
# Author: Nick Yang                #
# Date created: 5/9/2017           #
# Date last modified: 5/9/2017     #
# Python Version: 2.7              #
####################################


def P95_6(*args):
    avg = 1.0 * sum(args[0]) / len(args[0])
    return [max(args[0]), min(args[0]), avg]

t = (1, 2, 3, 4)
print P95_6(t)
