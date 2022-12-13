try:
    f=open('example.txt', 'r')
    print(f.read())
except FileNotFoundError:
    print('Something went wrong with opening the file.')
else:
    f.close()
