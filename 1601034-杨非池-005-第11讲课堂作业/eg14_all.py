def all_14_1(args):
    print args
    s = 0
    for i in args:
        s += i
    return s

def all_14_2(dic):
    print dic
    s = 0
    for i in dic.keys():
        s += dic[i]
    return s

t = [1,2,3]
print all_14_1(t)
t = (1,2,3,4,5,6)
print all_14_1(t)
t = {'x': 1, 'y': 2, 'c': 3}
print all_14_2(t)
