def digitize(num):
    if type(num)!=int:
        print('invalid input')
    else:
        l=[]
        for i in str(num):
            l.append(i)
    return tuple(l)

a,b,c,d=digitize(7325)
print(a,b,c,d)