def get_collection_builder(col_type):
    def f_tuple(a,b,c,d):
        new_tup=(a,b,c,d)
        return new_tup

    def f_list(a,b,c,d):
        new_list=[a,b,c,d]
        return new_list

    def f_set(a,b,c,d):
        new_set={a,b,c,d}
        return new_set

    if type(col_type)!=str:
        print('invalid input')

    elif col_type=="tuple":
        return f_tuple

    elif col_type=="list":
        return f_list

    elif col_type=="set":
        return f_set

    else:
        print('invalid input')


builder=get_collection_builder('list')
lst=builder(12,4,'r','11')
print(lst)




