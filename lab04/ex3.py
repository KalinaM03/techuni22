n=int(input('Enter how many numbers: '))
l=[]

for i in range (n):
    nums=int(input(f'Enter number{i+1}: '))
    l.append(nums)
print(l)

check=int(input('Enter 1 or 0: '))

if check==0:
    for i in range(len(l)):
        if i%2==0:
            l[i]+=5
    print(l)
elif check==1:
    for i in range(len(l)):
        if i%2!=0:
            l[i]+=10
    print(l)
else:
    print('invalid input')

