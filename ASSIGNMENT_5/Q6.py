### 6. Write a program to print first n prime numbers.

## using while loop.

# n = int(input('Enter n : '))
# count = 0
# num = 2
# while count < n :
#     i = 2
#     while i < num:
#         if num % i == 0:
#             break
#         i += 1
#     else:
#         print(num, end = ' ')
#         count += 1
#     num += 1 

## using for loop.

n = int(input('Enter n : '))
count = 0
num = 2
while count < n :
    for i in range(2, num):
        if num % i == 0: 
            break
    else:
        print(num, end = ' ')
        count += 1
    num += 1 