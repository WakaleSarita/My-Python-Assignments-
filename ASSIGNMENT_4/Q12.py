### 12. Write a program to check if given number is Armstrong number or not.  
### (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

## Using while loop.

# n = int(input('Enter a number: '))
# temp = n
# sum = 0

# digits = len(str(n))

# while n > 0:
#     digit = n % 10
#     sum += digit ** digits
#     n = n // 10

# if sum == temp:
#     print(temp, 'is an Armstrong number')
# else:
#     print(temp, 'is not a Armstrong number')


### Using for loop

n = int(input('Enter a number: '))
temp = n
sum = 0

num_str = str(n)
digits = len(num_str)

for ch in num_str:
    digit = int(ch)
    sum += digit ** digits


if sum == temp:
    print(temp, 'is an Armstrong number')
else:
    print(temp, 'is not a Armstrong number')



