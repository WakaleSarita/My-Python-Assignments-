### Write a program to swap two numbers without using third variable.

# input two numbers from users

a = int(input(' Enter first number :'))
b = int(input('Enter second number : '))

# display result before swapping

print(f'Befor swapping :- a:{a} , b:{b}')

# Swapping Values
 
a = a + b
b = a - b
a = a - b

# Display Result after swapping

print(f'After swapping :- a:{a}, b:{b}')
