n=int(input("Enter a number to check if it's prime: "))
counter=0

for i in range(1,n):
    if n%i==0:
        counter+=1
if counter==1:
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')
