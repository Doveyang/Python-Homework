def fun1(a, b, c):
    return a + b + c
def fun2(a, b, c, d):
    return a + b + c + d

tu = (1,2,3)
s = fun1(*tu)
print s
li = [1,2,3]
s = fun2(9,*li)
print s
