#
def square(a):
    if type(a)==int:
        area=a**2
        return area
    else:
        print('invalid input')

def rectangle(a,b):
    if type(a)==int and type(b)==int:
       area=a*b
       return area
    else:
        print('invalid input')

def right_triangle(a,b):
    if type(a)==int and type(b)==int:
       area=(a*b)/2
       return area
    else:
        print('invalid input')

shape=input('Enter a shape (square, rectangle or right triangle): ')

if shape=="square":
    a=int(input('Enter the side a: '))
    print(f'The area is {square(a)}.')
elif shape=='rectangle':
    a=int(input('Enter the side a: '))
    b=int(input('Enter the side b: '))
    print(f'The area is {rectangle(a,b)}.')
elif shape=='right triangle':
    a = int(input('Enter the side a: '))
    b = int(input('Enter the side b: '))
    print(f'The area is {right_triangle(a, b)}.')
else:
    print('invalid input')



