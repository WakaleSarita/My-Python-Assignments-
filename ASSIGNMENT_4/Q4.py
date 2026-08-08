### 4.  WAP to print factorial of a number .

## Using while loop

num = int(input('Enter Number : '))
i = 1
fact = 1
while(i <= num):
    fact *= i
    i += 1
print('Factorial = ', fact)


## Using for loop

num = int(input('Enter Number : '))
fact = 1
for i in range(1, num+1, 1):
    fact *= i
print('Factorial is : ',fact)
