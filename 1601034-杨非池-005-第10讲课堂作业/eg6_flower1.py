def flower(n):
    if int(n[0:1]) ** 3 + int(n[1:2]) ** 3 + int(n[2:3]) ** 3 == int(n):
        print 'Y'
    else:
        print 'N'

n = raw_input('Please input an number:')
flower(n)
