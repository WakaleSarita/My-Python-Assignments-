### 6. WAP to check if a given number is prime number or not. 

## Using While loop

# n = int(input('Enter number : '))
# i = 2 
# is_prime = True
# if n < 2:
#     is_prime = False
# while i < n:
#     if n % i == 0:
#         is_prime = False
#         break
#     i += 1
# print("Prime" if is_prime else 'Not prime')



## Using for loop 

num = int(input('Enter a number : '))
if num <= 1:
    print(num, 'is not a Prime Number')
else:
    is_prime = True
    for i in range(2, num): 
        if num % i == 0:
            is_prime = False
            break 
    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, 'is not a Prime Number')