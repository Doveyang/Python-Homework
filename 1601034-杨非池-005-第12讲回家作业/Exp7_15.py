# -*- coding:utf-8 -*-
####################################
# File name: Exp7_15.py            #
# Author: Nick Yang                #
# Date created: 5/15/2017          #
# Date last modified: 5/15/2017    #
# Python Version: 2.7              #
####################################
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
f = open('F7_15.txt', 'w')
s = u'''>Hi AaBbHi CcDdoO0Ll1a2a3a4a@#$Hi a>A Hi peach!=banana'''
f.write(s)
f.close()

f = open('F7_15.txt', 'r')
nA = 0
na = 0
n0 = 0
nr = 0
while True:
    x = f.read(1)
    if x == '':
        break
    if x.isupper():
        nA += 1
    elif x.islower():
        na += 1
    elif x.isdigit():
        n0 += 1
    else:
        nr += 1
f.close()
print '''
na = %s
nA = %s
n0 = %s
nr = %s
''' % (na, nA, n0, nr)
