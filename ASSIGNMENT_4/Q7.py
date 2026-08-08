### 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.  


## Using While loop 

# n = int(input('Enter a number : '))
# print("Numbers not divisible by 2 and 3 are : ")
# i = 1 
# while i <= n :
#     if i % 2 != 0 and i % 3 != 0:
#         print(i, end=' ')
#     i += 1


## Using For loop

n = int(input("Enter n : "))
print("Numbers not divisible by 2 and 3 are : ")
for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ")