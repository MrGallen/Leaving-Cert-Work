#Boolean - True/False
'''
>< >= <= == !=

5 > 10 - False

10 != 100 - True
'''
age = int(input('Enter your age - '))
# age = '18'
if int(age) < 17:
    print('You are not allowed to drive')
else:
    print('You can drive')
    
location = input('Enter where you are from - ').lower()
if location.lower() != 'donegal':
    print('Not from Donegal')
else:
    print('You are from donegal')
    
exam = int(input('Enter Grade - '))
if exam >= 90:
    print('H1')
elif exam >= 80:
    print('H2')
elif exam >= 70:
    print('H3')
elif exam >= 60:
    print('H4')
elif exam >= 50:
    print('H5')
else:
    print('Fail')
    
num1 = 33
num2 = 90
op = input('Op - ')
if op == '+':
    print(num1 + num2)
elif op == '-':
    
    
