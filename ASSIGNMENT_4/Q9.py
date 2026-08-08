### 9. WAP to print all numbers in a range divisible by a given number. 

## Using while loop:

# start = int(input('Enter start range: '))
# end = int(input('Enter end range: '))
# div = int(input('Enter divisor range: '))

# print('Number is divisible by ', div, ' are : ')
# i = start
# while i <= end:
#     if i % div == 0:
#         print(i, end=' ')
#     i += 1


## Using for loop.

start = int(input('Enter start range: '))
end = int(input('Enter end range: '))
div = int(input('Enter divisor range: '))

print('Number is divisible by ', div, ' are : ')
for i in range(start, end + 1):
    if i % div == 0:
        print(i, end=' ')

