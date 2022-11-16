n=int(input("enter a number: "))
tup=[]

while n>0:
    rem=n%10
    tup.append(rem)
    n//=10

tup1=tuple(tup)
print(tup1[::-1])
print(tup1)