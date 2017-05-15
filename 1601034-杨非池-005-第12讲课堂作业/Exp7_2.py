#coding=UTF-8
s = 'a1@中国\n'
f = open('F7_2.txt', 'w')
f.write(s)
f.seek(0, 2)
length = f.tell()
print u'文件长度=', length
