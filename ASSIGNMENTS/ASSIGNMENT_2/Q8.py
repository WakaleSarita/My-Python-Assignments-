### Write a Program to swap two numbers using third variable.

# input two numbers from users

a = int(input(' Enter first number : '))
b = int(input('Enter second number : '))

# display result before swapping

print(f'Befor swapping :- a:{a} , b:{b}')

# Swapping Values
 
c = b
b = a
a = c

# Display Result after swapping

print(f'After swapping :- a:{a}, b:{b}')



