###  Program to finds the Roots of a Quadratic Equation.

# Eplaination
# Quadratic Equetion = ax^2 + bx + c = 0
# Formula is :   Root = - b + or - square root of b^2- 4ac / 2a

# Take input for user

a = int(input('Enter Value of a : '))
b = int(input('Enter Value of b : '))
c = int(input('Enter Value of c : '))

# perform operation.

d = b ** 2 - (4 * a * c )

Root_1 = -b + (d ** 0.5) / 2 * a

Root_2 = -b - (d ** 0.5) / 2 * a

# Display Result 

print('The value of d is : ', d)
print('The root one is : ', Root_1)
print( 'The root two is : ', Root_2)




