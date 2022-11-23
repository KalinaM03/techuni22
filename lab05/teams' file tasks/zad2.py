def is_pal(num):
    return num==num[::-1]

num=input('Enter a number or a word to check if it is a palindrome: ')

answer=is_pal(num)

if answer:
    print(1)
else:
    print(0)