n=int(input('enter how many values you want to add to the dictionary:'))
d={}
for i in range(1,n+1):
    key=input(f'enter key {i}: ')
    value=input(f'enter value {i}: ')
    d[key]=value
print(f'Your dictionary: {d}')

m=int(input('Enter how many values you want to check: '))
m_list=[]

for i in range(1, m+1):
    m_key=input(f'enter value {i}:')
    if m_key in d:
        m_list.append(d[m_key])
        del d[m_key]
    else:
        m_list.append(m_key)

print(d)
print(m_list)
