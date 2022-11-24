def list_avg(lst, multiplier=1):
    num_list=[]
    if type(multiplier)!=int:
        print('invalid multiplier input')
    else:
        for i in lst:
            if type(i)==int or type(i)==float:
                num_list.append(i*multiplier)

    print(f'List average is {round((sum(num_list)/len(num_list)),2)}')
    return num_list

print(list_avg([2,4,'1','a',4],2))



