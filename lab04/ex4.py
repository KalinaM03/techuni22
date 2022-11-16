n = input("enter a number: ")
sum=0
last_number=0

for i in range(1,int(n)+1):
        sum+=int(n*i)
        last_number+=sum//10**(i-1)
        if i==int(n):
            print(n*i,"=",sum)
            break
        print(n*i,end=" + ")
