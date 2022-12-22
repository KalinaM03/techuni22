import Calculator

a = int(input('Enter a number: '))

if type(a) != int:
    print('Invalid input')

sign = input("Enter a '+', '-', '*', or '/' sign: ")

b = int(input('Enter another number: '))

if type(b) != int:
    print('Invalid input')

if sign == '+':
    print(Calculator.nsum(a,b))
elif sign == '-':
    print(Calculator.nsub(a,b))
elif sign == '*':
    print(Calculator.nmult(a,b))
elif sign == '/':
    print(Calculator.ndiv(a,b))
else:
    print('Invalid input')

