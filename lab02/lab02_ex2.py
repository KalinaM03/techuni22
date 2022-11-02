import math
print("Enter the radius "r" of a circle to calculate its circumference C and area S.")
r=float(input("r = "))
s=math.pi*(r**2)
c=2*math.pi*r
s = float(round(s,3))
c = float(round(c,3))
print("C =", c)
print("S =",s)
