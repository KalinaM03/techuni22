print("Enter 2 or 16 to convert 27102022 in one of those numerical systems.")

num=27102022
sys=int(input("Enter 2 or 16:"))
a=[]

if sys==2:
    while (num>0):
        b=num%2
        a.append(b)
        num=num//2
    a.reverse()
    for i in a:
        print(i, end="")

elif sys==16:
    while (num>0):
        b=num%16
        if b==10:
            b='A'
        elif b==11:
            b='B'
        elif b==12:
            b='C'
        elif b==13:
            b='D'
        elif b==14:
            b='E'
        elif b==15:
            b='F'
        a.append(b)
        num = num // 16
    a.reverse()
    for i in a:
        print(i, end="")
else:
    print('invalid number input')

