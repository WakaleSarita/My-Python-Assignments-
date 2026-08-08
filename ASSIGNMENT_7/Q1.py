# a. 

n = 5
for i in range(n):
    for k in range(n-i-1):
        print(' ', end = ' ')
    print('*', end = ' ')
        
    if i != 0:
        for k in range(2*i - 1):
            print(' ', end=' ')
        print('*', end =' ')
    print()


for i in range(n-2, -1, -1):

    for k in range(n-i-1):
        print(' ', end = ' ')
    print('*', end = ' ')
    if i != 0:
        for k in range(2*i - 1):
            print(' ', end = ' ')
        print('*', end = ' ')
    print()                                 # check it again

    
