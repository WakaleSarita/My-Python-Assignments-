### b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)  

## Using while loop

# n = int(input('Enter n : '))
# sum = 0
# i = 1

# while i <= n:
#     term = n ** i
#     sum += term
#     print(f'N^{i} = {term}')      ## ^ replace ** use karu shakato
#     i += 1
# print('Sum = ', sum)    


## Using for loop

n = int(input('Enter n : '))
sum = 0 
for i in range(1, n+1):
    term = n ** i
    sum += term
    print(f'N^{i} = {term}')

print('Sum = ', sum)