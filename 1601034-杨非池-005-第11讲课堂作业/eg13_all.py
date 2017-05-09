def all_5(**args):
    print args
    s = 0
    for i in args.keys():
        s += args[i]
    return s

print all_5(x=1,y=2,c=3)
