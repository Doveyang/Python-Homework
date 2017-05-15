#coding=UTF-8
import sys
reload(sys)
sys.setdefultencoding('utf-8')
f = open('F7_2.txt', 'r+')
s = u'文本文件的读取方法\n文本文件的写入方法\n'
f.write(s)
f.close
