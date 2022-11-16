n=int(input('enter a number: '))
l=[0,1]
n1=0
n2=1

for i in range(n):
    l.append(l[n1]+l[n2])
    n1+=1
    n2+=1

print(l)