n=int(input('Enter how many stars you want at the base of the triangle: '))
if n<0:
    print('invalid input')
else:
    for i in range(0,n):
        print('*'*(i+1))

