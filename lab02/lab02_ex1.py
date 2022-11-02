print('Enter the big base "a", the small base "b", and the height "h" of a trapezium to calculate its area S.')
a=float(input("a="))
b=float(input("b="))
h=float(input("h="))
s=(a+b)*h/2
s = float(round(s,2))
print('S =', s)