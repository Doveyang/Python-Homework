# -*- coding: cp936 -*-
dic = {'a': 'algorithm',
       'b': 'bug',
       'c': 'compile',
       'd': 'debugging',
       'e': 'exception'}

keyword = raw_input('������ؼ��֣�a~e��:')

while keyword >= 'a' and keyword <= 'e':
    print dic[keyword]
    keyword = raw_input('������ؼ��֣�a~e��:')
