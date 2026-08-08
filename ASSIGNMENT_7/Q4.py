# e.

#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5

n = 5
num = 1
for i in range(1, n+1):

    for k in range(n-i):
        print(' ', end=' ')
    
    for j in range(i):                  # increasing
        print(num + j, end = ' ')
    
    for j in range(i-2, -1 , -1):       # decreasing
        print(num+j, end=' ')
    num = num + 1
    print()