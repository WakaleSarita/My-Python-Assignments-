### Write a program to check whether the triangle is equilateral, isosceles or scalene triangle. 

# Take input from user.

a = float(input('Enter first side : '))
b = float(input('Enter second side : '))
c = float(input('Enter third side : '))

# Perform Condition

if( a + b > c) and ( b + c > a) and (a + c > b):
    if a == b == c:
        print(' Equilateral Triangle .')
    elif a == b or b == c or c == a:
        print('Isosceles Triangle')
    else:
        print('Scalene Triangle')
else:
    print('Invalid Traigle')        
