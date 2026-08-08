### 3.  WAP to print sum of series upto n. 

## Using While loop

num = int(input(' Enter Number : '))
i = 1
sum = 0
while(i <= num):
    sum += i
    i += 1
print('Sum =', sum)



## Using for loop

num = int(input('Enter number : '))
sum = 0
for i in range(1, num+1):
    sum += i
print('Sum =', sum)
    
    