### c. Find the sum of a geometric series from 1 to n where the common ratio is 2. 

## Using While loop

# n  = int(input('Enter n : '))
# sum = 0
# term = 1
# i = 0

# while i < n:
#     sum += term
#     print(term, end = ' ')
#     term *= 2
#     i += 1
# print('\n Sum = ', sum)


## Using for loop

n = int(input('Enter n : '))
sum = 0
term = 1 

for i in range(n):
    sum += term
    print(term, end = ' ')
    term *= 2

print(' \n Sum = ', sum)
