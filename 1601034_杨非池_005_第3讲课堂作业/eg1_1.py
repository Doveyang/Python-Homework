# -*- coding: UTF-8 -*-
list1 = [92,91,86,72,65,62,50,88,46,76]
list2 = [86,79,100,66,90,56]

list1.extend(list2)
print "合并后数据：" + str(list1)
list1.extend([66,90,56])
print "末尾添加三个数据后：" + str(list1)
list1.sort(reverse = True)
print u"降序排列后：" + str(list1)
