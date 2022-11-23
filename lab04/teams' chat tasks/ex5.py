import random
s=set(random.sample(range(20), 5))
s1=set(random.sample(range(20), 5))

print(s)
print(s1)

if s&s1:
    print("The sets have numbers in common. New set: ",s^s1)
else:
    print("The sets do NOT have numbers in common. New set: ",s|s1)