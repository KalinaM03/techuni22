def rhombus(a=1, ha=1):
    a = int(input('Enter the side a: '))
    ha = int(input('Enter the height ha: '))
    if type(a) != int or type(ha) != int or a < 0 or ha < 0:
        return f'Invalid input'
    return f'The area of the rhombus is {a*ha}'
