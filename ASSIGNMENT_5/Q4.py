### 4. WAP to print Armstrong number within a given range.

# Using while loop

# s = int(input('Start: '))
# e = int(input('End: '))
# num = s
# while num <= e:
#     temp = num 
#     sum = 0
#     digits = len(str(num))
#     while temp > 0:
#         sum += (temp % 10) ** digits
#         temp //= 10
#     if sum == num:
#         print(num)
#     num += 1

## Using for loop 

s = int(input('Start: '))
e = int(input('End: '))
for num in range(s , e+1):
    sum = 0
    for d in str(num):
        sum += int(d) ** len(str(num))
    if sum == num:
        print(num)
       