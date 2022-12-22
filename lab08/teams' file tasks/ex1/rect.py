def rectangle(a=1, b=1):
    a = int(input('Enter the side a: '))
    b = int(input('Enter the side b: '))
    if type(a) != int or type(b) != int or a < 0 or b < 0:
        return f'Invalid input'
    return f'The area of the rectangle is {a*b}'
