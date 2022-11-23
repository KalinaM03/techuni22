def n_sum(a,b):
    return a+b
def n_sub(a,b):
    return a-b
def n_div(a,b):
    return a/b
def n_mult(a,b):
    return a*b

op=input('enter an operation (+, -, *, or /): ')

a=int(input('enter first number: '))
b=int(input('enter second number: '))

if op=='+':
    print(n_sum(a,b))
elif op=='-':
    print(n_sub(a,b))
elif op=='*':
    print(n_mult(a,b))
elif op=='/':
    print(n_div(a,b))
else:
    print('invalid input')