#coding=GBK
s = 'a1@�й�\n'
f = open('F7_1.txt', 'w')
f.write(s)
f.seek(0, 2)
length = f.tell()
print '�ļ�����=', length
