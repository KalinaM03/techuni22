def num_list(lst,num):
    for i in lst:
        if type(i)==int:
            if i>num:
                lst[lst.index(i)]=0
    return lst


print(num_list([4,'2','a',5,18,24,2],10))