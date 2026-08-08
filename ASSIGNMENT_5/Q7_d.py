### d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10  

## USing While loop

# sum = 0
# i = 1
# while i <= 10:
#     a =int(input(f'Enter value for a{i} : '))
#     term = a / i
#     sum += term
#     i += 1

# print('Sum = ', sum)


## using for loop

sum = 0
for i in range (1, 11):
    a = int(input(f"Enter value for a{i}: "))
    term = a / i
    sum += term

print('Sum = ', sum)