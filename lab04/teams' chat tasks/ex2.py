# n=int(input('Enter a number: '))
# fact=1
#
# if n<0:
#     print('invalid input')
# elif n==0:
#     print(f'{n}! = ',1)
# else:
#     for i in range(1,n+1):
#         fact*=i
# print(f'{n}! = ', fact)
num = int(input("Enter N: "))
result = 1
for i in range(num, 0, -1):
    result *= i
print(result)