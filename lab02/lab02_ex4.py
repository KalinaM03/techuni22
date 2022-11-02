print("Enter a decimal number and the number of bit you want to know if it's a 0 or not.")
num=int(input("Decimal number:"))
bit=int(input("Enter bit:"))
if num & (1<<bit) != 0:
    print("True.")
else:
    print("False.")

