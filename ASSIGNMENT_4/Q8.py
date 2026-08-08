### 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range. 

## Using While loop 

# start = int(input('Enter start of range : '))
# end = int(input("Enter end of range: "))

# print('Numbers divisible by both 5 and 7: ')
# i = start
# while i <= end:
#     if i % 5 == 0 and i % 7 == 0:
#         print(i, end=' ')
#     i += 1

## Using For loop

start = int(input('Enter start of range : '))
end = int(input("Enter end of range: "))

print('Numbers divisible by both 5 and 7: ')
for i in range(start, end + 1):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=' ')
    