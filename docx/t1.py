def t(l, *args):
    if len(args) > 1:
        for i in args:
            print('em:%s' % i)
    else:
        print(args)
    print(l)


t(1, 2, 3)
