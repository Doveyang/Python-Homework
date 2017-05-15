#coding=UTF-8
import sys
reload(sys)
sys.setdefultencoding('utf-8')
f = open('F7_1.txt', 'r+')
f.seek(6)
f.write(u'央')
f.seek(1)
f.write('9')
f.seek(0,2)
f.write(u'人民政府')
f.close


