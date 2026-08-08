### e. x - x2/3 + x3/5 - x4/7 + …. to n terms 

## Using while loop

# x = int(input('Enter x : '))
# n = int(input('Enter n : '))
# sum = 0
# sign = 1
# i = 1

# while i <= n:
#     power = x ** i
#     denom = 2 * i - 1
#     term = sign * power / denom
#     sum += term
#     sign *= -1
#     i += 1

# print('Sum = ', sum)



## using for loop

x = int(input('Enter x : '))
n = int(input('Enter n : '))
sum = 0
sign = 1
for i in range(1, n+1):
    power = x ** i
    denom = 2 * i - 1
    term = sign * power / denom
    sum += term
    print(f'Term{i} = {term}')           ### check it again
    sign *= -1

print('Sum = ', sum)


