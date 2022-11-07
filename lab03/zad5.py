# задачата от часа

num = list(input("Enter a number: "))
order = input("Enter order: ")
new_num = ""

for i in order:
    new_num += num[int(i)-1]
print(f"New number: {new_num}")
