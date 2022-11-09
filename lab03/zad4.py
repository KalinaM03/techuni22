n=int(input("Enter a number to check if it's prime: "))

if n%2==0 and n!=2:
    print(f'{n} is not a prime number.')
elif n%3==0 and n!=3:
    print(f'{n} is not a prime number.')
elif n%5==0 and n!=5:
    print(f'{n} is not a prime number.')
elif n%7==0 and n!=7:
    print(f'{n} is not a prime number.')
elif n==1:
    print(f'{n} is not a prime number.')
else:
    print(f'{n} is a prime number.')