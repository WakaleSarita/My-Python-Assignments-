### 2. Enter number of students from user. For those many students accept marks of 5  
### subject marks from user and calculate percentage. Display all percentage and average percentage of students. 

## Using while loop

# n = int(input('Enter number of students: '))
# total_per = 0
# i = 1
# while i <= n:
#     sum = 0
#     j = 1
#     print('Enter 5 subject marks for students', i)
#     while j <= 5:
#         sum += int(input())
#         j += 1
#     per = sum / 5
#     print('percentage = ',per)
#     total_per += per
#     i += 1
# print('Average = ', total_per/n)


## Using for loop

n = int(input('Enter number of students: '))
total_per = 0
for i in range(1, n+1):
    sum = 0
    j = 1
    print('Enter 5 subject marks for students', i)
    for j in range(5):
        sum += int(input())
    per = sum / 5
    print('percentage = ',per)
    total_per += per
print('Average = ', total_per/n)
