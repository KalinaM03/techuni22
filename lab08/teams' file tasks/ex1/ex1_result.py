shape = input('Enter a shape: ')

if shape=='triangle':
    from trian import triangle
    print(triangle())
elif shape=='rectangle':
    from rect import rectangle
    print(rectangle())
elif shape=='square':
    from sqr import square
    print(square())
elif shape=='rhombus':
    from rhmb import rhombus
    print(rhombus())
elif shape=='trapezoid':
    from trap import trapezoid
    print(trapezoid())
else:
    print('Invalid input.')
