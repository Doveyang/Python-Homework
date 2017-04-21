# -*- coding:utf-8 -*-
####################################
# File name: P82_exam3.py          #
# Author: Nick Yang                #
# Date created: 4/21/2017          #
# Date last modified: 4/21/2017    #
# Python Version: 2.7              #
####################################
sentence = raw_input(u'请输入一段英文：')
if sentence.startswith('i '):
    sentence1 = 'I' + sentence[1:]
sentence2 = sentence1.replace(' i ', ' I ')
print sentence2
