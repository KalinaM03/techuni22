# задачата от дъската

start=int(input("Enter first number: "))
end=int(input('Enter last number: '))

while start<=end:
    if start%2==0 and start!=2:
        start += 1
    elif start%3==0 and start!=3:
        start += 1
    elif start%5==0 and start!=5:
        start += 1
    elif start%7==0 and start!=7:
        start += 1
    elif start==1:
        start += 1
    else:
        print(start)
        start+=1