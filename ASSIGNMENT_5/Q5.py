### 5. Write a program to print prime numbers between 1 to 100.  

## Using while loop.

# num = 2
# while num <= 100:
#     i = 2
#     while i < num:
#         if num % i == 0: 
#             break
#         i += 1
#     else:
#         print(num, end=" ")
#     num += 1

## Using for loop.

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0: 
            break
    else: 
        print(num, end=' ')