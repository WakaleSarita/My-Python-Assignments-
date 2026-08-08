### 1. WAP to print all even numbers until n.  

## Using while loop 

num = int(input('Enter number : '))
i = 2
while (i <= num):
    print(i, end = ' , ')
    i += 2




## Using for loop

num = int(input('Enter number  : '))
for i in range(2 , num+1 , 2):
    print(i, end = ' , ')
    

