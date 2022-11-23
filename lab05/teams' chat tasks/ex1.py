def input_nums(n):
    l = []
    if type(n) is not int:
        if n.isnumeric():
            n=int(n)
        else:
            return l
    else:
        for i in range(1,n+1):
            num=input(f'Enter number {i}: ')
            if num.isnumeric():
                l.append(int(num))
        return l

# print(input_nums('3'))


def sum_list(lst=[]):
    for i in lst:
        if type(i)==int or type(i)==float:
            continue
        elif i.isnumeric():
            lst[lst.index(i)]=int(i)
        else:
            lst.remove(i)

    return sum(lst)

# print(sum_list(['3','4',1]))

def max_of_two(a,b):
    if a==b:
        return a
    elif type(a) == int or type(a) == float:
        if type(b) != int:
            if type(b) != float:
                return a
            else:
                return max(a, b)
        else:
            return max(a, b)
    else:
        if type(b) != int:
            if type(b) != float:
                return
            else:
                return b
        else:
            return b

# print(max_of_two('a','5'))

# print(max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3))))
# Програмата създава 2 списъка, съгласно функцията input_nums(), като сумира елементите числа на отделните два списъка (от функцията sum_list()), след което връща по-големия от двата получени сбора (max_of_two()).


# print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))
# Програмата връща по-голямото от две числа - първото число е сумата на елементите числа от въведен списък във функцията sum_nums(), а второто е стринг, който може да бъде превърнат в число.
