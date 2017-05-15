#coding=GBK
s = 'a1@中国\n'
f = open('F7_1.txt', 'w')
f.write(s)
f.seek(0, 2)
length = f.tell()
print '文件长度=', length
