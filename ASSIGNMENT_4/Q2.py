### 2.  WAP to print all odd numbers until n.

## Using While loop

i = 1
num = int(input('Enter number : '))
while(i <= num):
    print(i , end = ' ')
    i += 2


    
## Using for loop

num = int(input('Enter number : '))
for i in range(1 , num+1, 2):
    print(i, end = ' ')