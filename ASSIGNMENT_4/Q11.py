### 11. WAP to check if given number Strong Number.

## Using while loop

# n = int(input('Enter a number : '))
# temp = n
# sum = 0
# while n > 0:
#     digit = n % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     sum += fact
#     n = n // 10
# if sum == temp:
#     print(temp, 'is a Strong Number')
# else:
#     print(temp, 'is not a Strong Number')

## Using for loop

n = int(input('Enter a number : '))
temp = n
sum = 0

num_str = str(n)

for ch in num_str:
    digit = int(ch)
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum += fact
    
if sum == temp:
    print(temp, 'is a Strong Number')
else:
    print(temp, 'is not a Strong Number')
