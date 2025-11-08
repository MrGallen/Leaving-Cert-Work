name = 'Eoin'
name2 = 'Danielle'
age = '29'

print(f'{name} is the age of {age}')
print(name2)

name = input('Please enter your name - ')
age = input(f'{name}, now can you enter your age - ')
print(f'{name},{age}')

#Boolean - True/False
'''
print(name == 'Harry')
if name == 'Harry':
    print('You are a son of the King')
elif name == 'Eoin':
    print('You teach CS')
elif name == 'Tom':
    print('You are a Cat')
else:
    print(f'Hi {name}')
'''    
if int(age) < 18:
    print('Not allowed')
else:
    print('Allowed Access')