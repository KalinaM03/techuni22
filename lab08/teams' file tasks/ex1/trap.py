def trapezoid(a=1, b=1, h=1):
    a = int(input('Enter the large base a: '))
    b = int(input('Enter the small base b: '))
    h = int(input('Enter the height h: '))
    if type(a) != int or type(b) != int or a < 0 or b < 0 or type(h) != int or h < 0:
        return f'Invalid input'
    return f'The area of the trapezoid is {((a*b)/2)*h}'
