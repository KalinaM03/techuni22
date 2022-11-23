#
def list_avg(lst=[], multiplier=1):
    if type(multiplier)!=int:
        print('invalid multiplier input')
    else:
        for i in lst:
            # lst.append(int(i)*multiplier)
            lst[lst.index(i)]=int(i)*multiplier
    return lst

print(list_avg([2,4,1],2))



