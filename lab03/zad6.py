# задачата от дъската

start=int(input("Enter first number: "))
end=int(input('Enter last number: '))

for i in range(start,end+1):
    counter = 0
    for n in range(i):
        if i%(n+1)==0:
            counter+=1
    if counter==2:
        print(i)


