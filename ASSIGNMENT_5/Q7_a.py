### 7. Write a program to solve the following series :  
# a. 1! + 2! + 3! + 4! + …..n!  
# b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)  
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.  
# d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10  
# e. x - x2/3 + x3/5 - x4/7 + …. to n terms 

# a 
## Using while loop

# n = int(input("Enter n : "))
# sum = 0 
# i = 1

# while i <= n:
#     fact = 1
#     j = 1
#     while j <= i:
#         fact *= j
#         j += 1
#     sum += fact
#     print(f'{i} = {fact}')
#     i += 1

# print('Sum = ', sum)



## Using for loop

n = int(input('Enter n: '))
sum = 0
for i in range(1, n+1):
    fact = 1 
    for j in range(1, i+1):
        fact *= j 
    sum += fact
    print(f'{i} != {fact}')
print("sum = " , sum)