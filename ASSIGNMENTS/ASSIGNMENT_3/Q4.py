### Write a program to input all sides of a triangle and check whether triangle is valid or not.

# Take input sides of the traingle from user.

a = float(input('Enter first side : '))
b = float(input('Enter second side : '))
c = float(input('Enter third side : '))

# Perform condition and display result.

if(a + b > c) and (b + c > a) and (a + c > b):
    print('Triangle is valid.')
else:
    print('Triangle is not valid.')
    