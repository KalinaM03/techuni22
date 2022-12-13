import math

try:
    n=int(input('Enter a number to see the square root of: '))
    if n<0:
        raise ValueError()
    else:
        print(f'The square root of {n} is {math.sqrt(n)}.')
except ValueError:
    print('Invalid number.')
finally:
    print('Good bye!')
