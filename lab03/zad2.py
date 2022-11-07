n=int(input('Enter how many numbers you want to sum: '))
num_sum=0
if n<0:
    print('invalid input')
else:
    for i in range (0, n):
        num=int(input(f'Enter number {i+1}: '))
        num_sum+=num
    print(f'The sum is {num_sum}')
