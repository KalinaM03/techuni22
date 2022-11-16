import random

nums=int(input("Enter how many numbers in the list: "))
range_nums=int(input("Enter end range of the numbers: "))
list_nums=[]

for i in range(nums):
    list_nums.append(random.randrange(range_nums))
print(list_nums)

place=0
for i in range(nums-1):
    list_nums.insert(place+1, list_nums[place]+list_nums[place+1])
    place+=2
print(list_nums)