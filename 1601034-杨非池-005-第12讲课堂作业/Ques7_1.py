# -*- coding: utf-8 -*-
f = open('Ques7_1.txt', 'w')
f.write('姓名'+'\t'+'性别'+'\t'+'电话'+'\t'+'\t'+'地址\n')
flag = 'y'
while flag == 'y':
    name = raw_input(u'请输入姓名：')
    sex = raw_input(u'请输入性别：')
    phone = raw_input(u'请输入电话：')
    address = raw_input(u'请输入住址：')
    f.write(name + '\t' + sex + '\t' + phone + '\t' + address + '\n')
    flag = raw_input(u'是否继续输入 y/n ?')
f.close()
