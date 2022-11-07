n=int(input("Enter how many numbers you want to compare: "))
max_n=0
if n<0:
    print('invalid input')
else:
    for i in range(0,n):
        num=int(input(f'Enter number {i+1}:'))
        if num>max_n:
            max_n=num
    print(f'the largest number is {max_n}')