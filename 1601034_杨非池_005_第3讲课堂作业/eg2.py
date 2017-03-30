# -*- coding: UTF-8 -*-
data_list = [12.0,12.5,11.7,12.6,13.5,12.8,12.0,12.0,11.4,12.0]

print "一共有%r个数据，分别为：%r" % (len(data_list), data_list)

print "销售量为12.0的个数:%r" % data_list.count(12.0)

print "销售总额为:%s" % sum(data_list)
 
print "销售量最小值：%s" % min(data_list)

data_list.remove(min(data_list))

print "删除最小值后的数据：%r" % data_list
