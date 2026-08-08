### 5. WAP to print Fibonacci series upto n.  

## Using while loop

# n = int(input('Enter number n : '))
# a, b = 0 , 1
# i = 0
# while( i < n):
#     print(a, end = ' ')
#     a , b = b ,a+b
#     i += 1


## Using for loop

# n = int(input('Enter fibonacci number : '))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b , a+b

## 2

n = int(input('Enter fibonacci number : '))
a = -1
b = 1
for i in range(n):
    c = a+b
    print(c , end =' ')
    a = b
    b = c
