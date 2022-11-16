n=int(input("enter a number: "))
lis=[]
dic={}

while n>0:
    counter=0
    lis.append(n-counter)
    n-=1
    counter+=1

print(lis[::-1])

counter_keys=-1
counter_vals=0

for i in range(len(lis)):
    dic[lis[counter_keys]]=lis[counter_vals]
    counter_keys-=1
    counter_vals+=1

for k,v in dic.items():
    print(f"{k}:{v}", end=" ")


