text=input("Enter text: ")
dic={}

for i in text:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for k,v in dic.items():
    print(f"{k}:{v}", end=" ")