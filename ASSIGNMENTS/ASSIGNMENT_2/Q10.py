### Write a program to reverse three-digit number.

# Take Values from user

num = int(input(' Enter three digits number :'))

digit1 = num % 10
digit2 = (num // 10) % 10
digit3 = num // 100

reverse_number = digit1 * 100 + digit2 * 10 + digit3

# Display Result

print('Reversed number =', reverse_number)





