def square(a=1):
    a = int(input('Enter the side a: '))
    if type(a) != int or a < 0:
        return f'Invalid input'
    return f'The area of the square is {a**2}'
